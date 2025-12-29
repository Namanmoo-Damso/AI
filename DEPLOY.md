# Deploying the AI agent

This document shows simple ways to run the AI agent as a standalone service.

Prerequisites

- A server with Docker and Docker Compose installed (or Python 3.11+ and pip).
- A LiveKit server reachable from this host (if you want real-time audio/video).
- An OpenAI API key for the OpenAI plugin.

Quick start (Docker Compose)

1. Copy `.env.example` to `.env` and fill values:

```bash
cp .env.example .env
# edit .env and add OPENAI_API_KEY, LIVEKIT_* values
```

2. Build and run with Docker Compose:

```bash
docker compose up -d --build
```

3. Check logs:

```bash
docker compose logs -f ai-agent
```

Run locally (no Docker)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env
python main.py
```

Notes

- This repository contains the LiveKit agent worker (`main.py` / `simple_agent.py`).
- If you want this to run as a separate service in production, deploy behind a process supervisor
  or container orchestrator and ensure secrets are stored securely (e.g., environment variables
  in your cloud provider, or a secret manager).

Pushing to GitHub

To push this prepared repository to `git@github.com:Namanmoo-Damso/AI.git` from your machine:

```bash
cd path/to/AI
git init
git remote add origin git@github.com:Namanmoo-Damso/AI.git
git add .
git commit -m "Initial import: AI agent from AI"
git branch -M main
git push -u origin main
```

If you'd like, I can attempt to set the remote and push from this environment — say so explicitly.
