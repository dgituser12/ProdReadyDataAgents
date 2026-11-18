# Changelog

## Orchestration v2

- Preserved the v1 synthetic data, metrics, semantic catalogue, BigQuery tools and inventory Skill.
- Added supplier-performance and fulfilment-exposure Skills.
- Added a single-agent ADK factory for the beginner learning path.
- Added Inventory, Supplier and Fulfilment specialist ADK agents with scoped tools.
- Added an ADK coordinator with `single_turn` specialist sub-agents.
- Added explicit `CROSS_DOMAIN` routing; retained `UNCERTAIN` for ambiguous/unsupported requests.
- Added deterministic specialist planning, bounded delegation-plan validation and multi-agent evaluation fixtures.
- Added Track A coordinator wrappers around one injected managed Conversational Analytics data agent.
- Expanded documentation to distinguish prompt scoping from IAM/security boundaries and local tests from live integration.
