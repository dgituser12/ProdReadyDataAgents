# Enterprise Data Agents on Google Cloud — GDG Essex

**Workshop:** From Data to Action: Building Enterprise Data Agents with Google Cloud  
**Format:** 150-minute hands-on workshop  
**Learning path:** single Data Agent → domain specialists → coordinator-led multi-agent system

This is the consolidated workshop codebase. It combines the original v1 data foundation with the v2 progressive agent architecture. There is one copy of each shared component; v1 and v2 are not separate participant downloads.

> **Current status:** This repository is the pre-notebook technical baseline. The four Colab notebooks will be added after the ADK and Google Cloud integration checks in [TESTING.md](TESTING.md) have been completed.

## Learning architecture

1. **Beginner — single agent:** one focused, read-only Data Agent answers a business question using approved tools and canonical business definitions.
2. **Intermediate — specialists:** Inventory, Supplier and Fulfilment specialists receive domain-specific instructions, Skills and narrow tool allow-lists.
3. **Advanced — coordinator:** an ADK coordinator delegates to one or more specialists and synthesises their evidence for cross-domain questions.

## Repository contents

| Path | Purpose |
|---|---|
| `data/` | Synthetic Essex distribution-centre CSV data and manifest |
| `scripts/` | Generate, validate, load and calculate business metrics |
| `semantic_catalogue/` | Canonical metric definitions, glossary and BigQuery views |
| `tools/` | Read-only, parameterised BigQuery business tools |
| `skills/` | Inventory, Supplier and Fulfilment Agent Skills |
| `orchestration/` | Routing, route policy, delegation planning and ADK agent factories |
| `evals/` | Labelled routing and specialist-selection fixtures |
| `tests/` | Unit tests for data, metrics, tools, skills and orchestration |
| `docs/` | Architecture and implementation notes |

## Quick start — local checks

The data generator, validator, metric calculator, routing baselines and unit tests use Python's standard library. BigQuery and ADK integrations are optional until you run the live-cloud checks.

```bash
git clone https://github.com/<your-github-username>/enterprise-data-agents-gdg-essex.git
cd enterprise-data-agents-gdg-essex

python scripts/validate_data.py --input-dir data/sample
python scripts/calculate_metrics.py --input-dir data/sample
python scripts/evaluate_router.py
python scripts/evaluate_multi_agent.py
python -m unittest discover -s tests -v
```

See [TESTING.md](TESTING.md) for the full validation sequence and expected results.

## Synthetic business scenario

The sample dataset represents **Essex Central Distribution Centre** (`WH-ESSEX-01`), with GBP as the currency and a snapshot date of `2026-10-01`.

- 8 suppliers
- 60 products
- 60 inventory snapshot rows
- 500 fulfilment orders

The data is synthetic and intended for education. The business definitions in `semantic_catalogue/` are authoritative for this workshop.

Important metric distinctions:

- Inventory value at risk = shortage units × unit cost; it is not lost revenue.
- Supplier profile risk tier is distinct from observed delivery performance.
- Late delivered orders are distinct from overdue open orders.
- Lead time is modelled at supplier level.

## Google Cloud and agent setup

The live agent track targets the versions in `requirements-agent.txt`. Install those dependencies only when you are ready to run the ADK and BigQuery integration checks:

```bash
python -m pip install -r requirements-agent.txt
```

You will also need a Google Cloud project, the required APIs and IAM permissions, and Application Default Credentials (ADC). In Colab, use the supported user authentication flow. Do not upload or commit service-account JSON keys.

The BigQuery loader is explicit about dataset creation and write mode. Review its arguments before running it against a project. The agent-facing query tools are read-only and use fixed SQL, typed parameters and row/bytes limits.

## Two implementation tracks

- **Track A — Managed Conversational Analytics + ADK:** an injected managed data-agent callable is wrapped by ADK. The coordinator example uses three domain-scoped ADK wrappers over one configured managed data agent; these are not three separately provisioned managed resources. Prompt scopes are not security boundaries.
- **Track B — ADK + BigQuery:** custom ADK agents use the shared read-only BigQuery tools, semantic catalogue and Agent Skills.

The managed Conversational Analytics resource and its permissions are configured in the user's Google Cloud environment and are not stored in this repository.

## Safety and scope

- Workshop agents and tools are read-only. No purchasing, stock mutation, supplier contact or other business write action is implemented.
- Never commit API keys, access tokens, credentials, real customer data or local `.env` files.
- Skills provide task guidance; they are not security controls. IAM, data permissions and tool allow-lists remain essential.
- A passing local test suite is not proof of a live cloud integration or production readiness.

## Public repository setup

1. Create a **public** repository in your personal GitHub account named `enterprise-data-agents-gdg-essex`.
2. Push this repository's contents to the `main` branch.
3. Replace `<your-github-username>` in this README with your GitHub username.
4. Add the four Colab notebooks and their **Open in Colab** links after the integration validation gate is complete.
5. Tag the eventual participant-ready workshop snapshot as a GitHub release.

## Licence

Add the licence you intend to publish this material under before making the repository public. No licence has been selected in this starter package.
