# DEV_GUIDE — Formatting & Editor setup

This repo follows the team's standard code style. Please install the recommended VS Code extensions (see `.vscode/extensions.json`).

Quick setup:

```bash
# Create venv and install deps (Python)
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Formatting workflow

- Prettier is used for JS/TS formatting. Files are formatted on save.
- Python is formatted with Black on save in VS Code.
- Keep `.env` out of version control; use `.env.example` as template.

Commit hooks (optional)

Consider adding `pre-commit` with `black`, `ruff`, and `prettier` to enforce formatting locally.
