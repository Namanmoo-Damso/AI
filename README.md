# test_backend_ios-ai

This repository contains the AI agent extracted from the main `test_backend_ios` project. It includes the voice agent worker that connects to LiveKit and uses OpenAI for STT/LLM/TTS via the LiveKit plugins.

Quick start

1. Create a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create a `.env` file next to `main.py` / `simple_agent.py` and add your `OPENAI_API_KEY` and any LiveKit config required by your environment.

3. Run the worker:

```bash
python main.py
# or
python simple_agent.py
```

Notes

- The agent expects LiveKit and the LiveKit agent plugins to be available.
- Adjust `requirements.txt` to pin versions matching your deployment.
