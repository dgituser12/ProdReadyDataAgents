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

## 2026-11-19 — Notebook 2

- Added a 35-minute Colab lab for semantic grounding, Agent Skills, scoped read-only tools, three ADK specialists and deterministic routing preview.
- Reused the shared participant bootstrap and configuration pattern.

## Notebook 3 — Multi-agent system

- Added a 35-minute Colab-first lab that assembles the three domain specialists under an ADK coordinator.
- Includes single-domain and cross-domain execution, event-trace inspection, deterministic planning comparison, fixture evaluation, failure/guardrail review and a participant challenge.
- Includes explicit mapping to the ten workshop concepts and preserves the 150-minute facilitation schedule.

## Notebook 3 — Multi-agent system

- Added a 35-minute Colab-first lab that assembles the three domain specialists under an ADK coordinator.
- Includes single-domain and cross-domain execution, event-trace inspection, deterministic planning comparison, fixture evaluation, failure/guardrail review and a participant challenge.
- Includes explicit mapping to the ten workshop concepts and preserves the 150-minute facilitation schedule.

## Optional integration and Data Harness completion

- Added a governed Data Harness package with semantic metric resolution, source adapter contract, BigQuery semantic-view adapter and policy checks.
- Added optional ADK DataAgentToolset bridge for a pre-configured Conversational Analytics Data Agent.
- Added optional Gemini Decision 1 client factory, explicitly separate from Vertex AI ADC.
- Added optional BigQuery Agent Analytics ADK plugin wiring and a Colab appendix example.
- Added Notebook 2 Data Harness execution exercises and Notebook 3 opt-in integration appendix; all optional switches default to disabled.


## 2026-11-19 — Decision 1 structured exception assessment

- Expanded the optional Notebook 3 Decision 1 lab from single-label route classification to three typed questions about one supply-chain exception dossier: primary domain (`choice`), urgency (`noul`) and severity (`score`).
- Added confidence inspection, configurable threshold, deterministic route fallback, and safe omission of urgency/severity when confidence is low or the API fails.
- Added unit tests for the single-request contract, low-confidence fallback and API-error fallback.
- Core workshop remains unchanged; the optional section is disabled by default and does not add time to the 150-minute agenda.
