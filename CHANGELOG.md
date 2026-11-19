# Changelog

## Colab-first shared setup architecture
- Replaced participant Notebook 0 with reusable `setup/workshop_setup.py` and non-secret YAML configuration.
- Practical notebooks bootstrap the repository and dependencies from inside Colab, then initialise ADC, Vertex AI, BigQuery copies and semantic views.
- Existing tables and views are preserved on reruns; no API key is required for the Vertex AI path.
- Standardised the workshop title as **Building Production-Grade Data Agents on GCP** and removed level labels from notebook titles.


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

## Participant configuration cell refresh
- Separated repository bootstrap/dependency installation from the single participant-editable configuration cell in Notebook 1.
- Configuration is written to the Colab runtime clone; participants do not edit GitHub files or manually open YAML.
- Removed duplicate introductory learning-objective and mental-model sections.
