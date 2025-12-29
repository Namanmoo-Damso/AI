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

Pre-commit setup (recommended)

1. Install locally (inside your venv):

```bash
pip install pre-commit
```

2. Install the git hooks (run once per checkout):

```bash
pre-commit install
```

3. To run against all files (e.g., before first commit):

```bash
pre-commit run --all-files
```

This repo includes `.pre-commit-config.yaml` and `pyproject.toml` for Black, Ruff, isort, and Prettier.
