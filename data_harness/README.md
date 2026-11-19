# Governed Data Harness

The Data Harness is a governed data-access layer between agents and enterprise sources. It separates the agent from source-specific connection logic and enforces a semantic and policy contract before data is returned.

## Included implementation

- `SemanticCatalogue` resolves canonical metric IDs, units, interpretations and caveats from `semantic_catalogue/metrics.json`.
- `HarnessPolicy` allow-lists sources and metric IDs and defaults to read-only access.
- `DataSourceAdapter` defines the contract for additional source adapters.
- `BigQuerySemanticViewAdapter` is the working workshop adapter. It only reads a fixed allow-list of approved semantic views with a bounded row limit.
- `GovernedDataHarness` resolves the metric, checks policy and invokes the selected adapter.

## Extending to federated sources

Implement `fetch_metric(metric_id, parameters)` for another source and register it by a source name. Add the source name and permitted metric IDs to `HarnessPolicy`. Do not expose raw connection credentials or unrestricted SQL to the agent. A real additional source still requires its own network connectivity, identity, IAM/ACLs, source-side policies, audit logging and integration tests.

The workshop demonstrates the adapter and governance pattern using BigQuery. It does not provision a live cross-cloud federation service.
