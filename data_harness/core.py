"""Governed Data Harness: semantic routing and policy-enforced source adapters.

The workshop ships a working BigQuery adapter and a source-adapter contract.
Additional federated systems can implement the same interface without changing
agent-facing tools. This module does not provision or claim live federation.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol


class DataSourceAdapter(Protocol):
    """Minimal adapter contract for a governed data source."""
    source_name: str
    def fetch_metric(self, metric_id: str, parameters: dict[str, Any]) -> dict[str, Any]: ...


@dataclass(frozen=True)
class HarnessPolicy:
    allowed_sources: tuple[str, ...] = ("bigquery",)
    allowed_metric_ids: tuple[str, ...] = ()
    max_rows: int = 100
    read_only: bool = True

    def validate(self, source_name: str, metric_id: str) -> None:
        if not self.read_only:
            raise PermissionError("Workshop Data Harness is read-only.")
        if source_name not in self.allowed_sources:
            raise PermissionError(f"Source '{source_name}' is not approved by policy.")
        if self.allowed_metric_ids and metric_id not in self.allowed_metric_ids:
            raise PermissionError(f"Metric '{metric_id}' is not approved by policy.")


class SemanticCatalogue:
    """Loads canonical metric definitions and resolves IDs to governed metadata."""
    def __init__(self, path: str | Path):
        self.path = Path(path)
        self.document = json.loads(self.path.read_text(encoding="utf-8"))
        self.metrics = {m["id"]: m for m in self.document.get("metrics", [])}

    def get_metric(self, metric_id: str) -> dict[str, Any]:
        try:
            return self.metrics[metric_id]
        except KeyError as exc:
            raise KeyError(f"Metric '{metric_id}' is not in the semantic catalogue.") from exc


class BigQuerySemanticViewAdapter:
    """Read-only BigQuery adapter restricted to an explicit metric->view map."""
    source_name = "bigquery"

    METRIC_VIEW_MAP = {
        "inventory.products_below_safety_stock": "v_inventory_risk_summary",
        "inventory.shortage_units": "v_inventory_risk_summary",
        "inventory.value_at_risk_gbp": "v_inventory_risk_summary",
        "supplier.on_time_delivery_rate": "v_supplier_delivery_performance",
        "supplier.late_deliveries": "v_supplier_delivery_performance",
        "supplier.average_late_days": "v_supplier_delivery_performance",
        "fulfillment.overdue_open_orders": "v_fulfillment_risk_summary",
        "fulfillment.delayed_open_order_value_gbp": "v_fulfillment_risk_summary",
    }

    def __init__(self, project_id: str, dataset_id: str, location: str = "US", client: Any | None = None):
        if client is None:
            from google.cloud import bigquery
            client = bigquery.Client(project=project_id, location=location)
        self.client = client
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.location = location

    def fetch_metric(self, metric_id: str, parameters: dict[str, Any] | None = None) -> dict[str, Any]:
        if metric_id not in self.METRIC_VIEW_MAP:
            raise KeyError(f"No governed BigQuery view mapping for metric '{metric_id}'.")
        view = self.METRIC_VIEW_MAP[metric_id]
        sql = f"SELECT * FROM `{self.project_id}.{self.dataset_id}.{view}` LIMIT @row_limit"
        from google.cloud import bigquery
        job_config = bigquery.QueryJobConfig(query_parameters=[
            bigquery.ScalarQueryParameter("row_limit", "INT64", min(int((parameters or {}).get("limit", 100)), 100))
        ])
        rows = [dict(row.items()) for row in self.client.query(sql, job_config=job_config, location=self.location).result()]
        return {"source": self.source_name, "view": view, "metric_id": metric_id, "rows": rows}


class GovernedDataHarness:
    """Resolve semantics, enforce source/metric policy, then call an adapter."""
    def __init__(self, catalogue: SemanticCatalogue, adapters: dict[str, DataSourceAdapter], policy: HarnessPolicy):
        self.catalogue = catalogue
        self.adapters = adapters
        self.policy = policy

    def invoke_tool(self, metric_id: str, tool_callable: Any, parameters: dict[str, Any] | None = None, source_name: str = "bigquery") -> dict[str, Any]:
        """Invoke a pre-approved read-only tool through semantic and policy checks."""
        metric = self.catalogue.get_metric(metric_id)
        self.policy.validate(source_name, metric_id)
        if not callable(tool_callable):
            raise TypeError("tool_callable must be callable")
        evidence = tool_callable(**(parameters or {}))
        return {
            "metric": {"id": metric["id"], "name": metric["name"], "unit": metric["unit"], "interpretation": metric["interpretation"], "caveats": metric.get("caveats", [])},
            "evidence": evidence,
            "policy": {"source": source_name, "read_only": self.policy.read_only, "max_rows": self.policy.max_rows},
        }

    def retrieve(self, metric_id: str, source_name: str = "bigquery", parameters: dict[str, Any] | None = None) -> dict[str, Any]:
        metric = self.catalogue.get_metric(metric_id)
        self.policy.validate(source_name, metric_id)
        if source_name not in self.adapters:
            raise KeyError(f"No adapter is registered for source '{source_name}'.")
        bounded_parameters = dict(parameters or {})
        requested_limit = int(bounded_parameters.get("limit", self.policy.max_rows))
        bounded_parameters["limit"] = max(1, min(requested_limit, self.policy.max_rows))
        result = self.adapters[source_name].fetch_metric(metric_id, bounded_parameters)
        return {
            "metric": {"id": metric["id"], "name": metric["name"], "unit": metric["unit"], "interpretation": metric["interpretation"], "caveats": metric.get("caveats", [])},
            "evidence": result,
            "policy": {"source": source_name, "read_only": self.policy.read_only, "max_rows": self.policy.max_rows},
        }


def build_bigquery_harness(project_id: str, dataset_id: str, catalogue_path: str | Path, location: str = "US") -> GovernedDataHarness:
    catalogue = SemanticCatalogue(catalogue_path)
    allowed_ids = tuple(BigQuerySemanticViewAdapter.METRIC_VIEW_MAP.keys())
    adapter = BigQuerySemanticViewAdapter(project_id, dataset_id, location)
    policy = HarnessPolicy(allowed_sources=("bigquery",), allowed_metric_ids=allowed_ids, max_rows=100, read_only=True)
    return GovernedDataHarness(catalogue, {"bigquery": adapter}, policy)
