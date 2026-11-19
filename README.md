# **Building Production-Grade Data Agents on GCP**

GDG Essex workshop · 150 minutes · Google Colab participant experience

## Start here

Open any practical notebook directly in Google Colab from the public GitHub repository. Each practical notebook has a first cell that clones the repository (if necessary), installs dependencies, writes the participant configuration and calls the shared `setup/workshop_setup.py` module.

**There is no separate Notebook 0.** The practical notebooks are independently launchable. Participants do not need a terminal, local IDE, manual Git commands or a Gemini API key.

## Notebook sequence

| Notebook | Purpose |
|---|---|
| 1 — Build Your First Enterprise Data Agent | Build a read-only Gemini + ADK agent over BigQuery |
| 2 — Give Your Agent Enterprise Expertise | Zetaris-inspired Data Harness, semantic catalogue, Agent Skills and three specialists |
| 3 — Build the Multi-Agent System | Coordinator, bounded delegation, guardrails, evaluation and observability |
| 4 — Enterprise Reference Hub | Production architecture, security, federation, memory and advanced integrations |

Notebook titles intentionally do not use labels such as beginner, intermediate or advanced. The learning progression is expressed through the material and exercises.

## Shared setup architecture

- `setup/workshop_setup.py`: shared authentication, Vertex AI configuration, BigQuery dataset preparation, server-side table copies, semantic view creation and validation.
- `config/workshop_config.yaml`: participant-editable, non-secret project/model/source identifiers.
- `config/workshop_config.example.yaml`: configuration template.
- `requirements-agent.txt`: pinned compatible ADK / Google Gen AI / BigQuery dependencies.

The setup is idempotent:
- Existing destination tables are never overwritten.
- Existing semantic views are not replaced automatically.
- Re-running setup validates the environment and reuses existing resources.

Authentication uses Google Colab ADC and explicitly configures Vertex AI (`GOOGLE_GENAI_USE_VERTEXAI=TRUE`). The Gemini model location (`global`) is separate from the BigQuery dataset location (`US`).

## Workshop scenario

Essex Central Distribution Centre (`WH-ESSEX-01`), synthetic data, snapshot `2026-10-01`, currency GBP:
- 8 suppliers
- 60 products
- 60 inventory snapshot rows
- 500 fulfilment orders

Tables: `suppliers`, `products`, `inventory_snapshot`, `fulfillment_orders`.

Semantic views:
- `v_inventory_product_risk`
- `v_supplier_delivery_performance`
- `v_fulfillment_order_exposure`
- `v_inventory_risk_summary`
- `v_fulfillment_risk_summary`

Business definitions: inventory value at risk = shortage units × unit cost (not lost revenue); supplier profile risk tier is distinct from observed delivery performance; late delivered orders differ from overdue open orders.

## Architecture choices

- Core implementation: ADK + BigQuery, read-only tools.
- Managed comparison: Conversational Analytics, optional and subject to service/API verification.
- Optional routing: Decision 1 model, with deterministic fallback.
- Observability: Colab traces as baseline; BigQuery Agent Analytics as an optional advanced integration.
- Data Harness: Zetaris-inspired governed/federated data-access pattern demonstrated with BigQuery, semantic views, semantic catalogue and scoped tools. The workshop does not deploy Zetaris or claim live cross-cloud federation.

## Organiser publication checklist

1. Create a public GitHub repository named `enterprise-data-agents-gdg-essex`.
2. Replace the repository URL placeholder in the first cell of each practical notebook.
3. Publish a source BigQuery dataset in US containing the four workshop tables.
4. Update source project/dataset placeholders in `config/workshop_config.yaml` and the notebook bootstrap cell.
5. Grant participants source dataset read access and appropriate permissions in their own Google Cloud projects.
6. Test each notebook from a fresh Colab runtime.
7. Add “Open in Colab” links once the final repository URL is known.

Maintainer scripts and unit tests are for repository maintenance; they are not part of the participant workflow.
