# GDG Essex — Enterprise Data Agents workshop assets

Synthetic supply-chain dataset, generation/validation/loading scripts, canonical business metrics and semantic catalogue for the 150-minute Google Cloud Data Agents workshop.

## Quick start

```bash
python scripts/generate_data.py
python scripts/validate_data.py --input-dir data/sample
python scripts/calculate_metrics.py --input-dir data/sample --output data/sample/business_metrics.json
```

See `data/README.md`, `scripts/README.md` and `semantic_catalogue/README.md` for details. All data is synthetic. BigQuery loading requires `google-cloud-bigquery` and Google Application Default Credentials; no service-account key file is required or included.
