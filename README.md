# MG Advisory Finance OS

Clean V1 foundation for an institutional finance SaaS: FastAPI backend, lightweight HTML/CSS/JS frontend, project storage, document upload, basic financial normalization, and openpyxl-based Excel business plan generation.

The web interface is a commercial-style SaaS workspace with secure license login, dashboard, project library, active project workspace, data-room upload, output generation, templates status, and optional Claude AI brief generation.

The Excel generator produces a driver-based institutional BP model with monthly periods, upload/data-room mapping, revenue streams, product/service build, headcount, opex, working capital, capex, debt config, debt schedule, financial statements, covenants, outputs, checks, and a final `Lists & Dates` sheet for fixed dates and validation lists.

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

Default license key:

```text
MG-ADVISORY-DEMO-2026
```

Override it in Railway with:

```text
MG_LICENSE_KEY=your-production-license
```

Optional Claude integration:

```text
ANTHROPIC_API_KEY=your-anthropic-api-key
ANTHROPIC_MODEL=claude-3-5-sonnet-latest
```

If `ANTHROPIC_API_KEY` is not set, the app still starts and the AI brief endpoint returns a local fallback.

## Railway

Railway uses:

- `railway.json` for the start command
- `Procfile` as a fallback start command
- `runtime.txt` for Python version
- `requirements.txt` for dependencies

Persisted files are written to `data/projects` and generated outputs to `outputs`. For production, connect these paths to durable storage or S3-compatible object storage.

Legacy reference templates from the prior GitHub working repo are included under `templates/legacy`.
