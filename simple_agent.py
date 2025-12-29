from pathlib import Path
from dotenv import load_dotenv
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
)

from livekit.agents.voice import Agent, AgentSession
from livekit.plugins import openai, silero
import logging

load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Set logging to DEBUG to see all timing information
logging.basicConfig(level=logging.DEBUG)


async def entrypoint(ctx: JobContext):

    print(f"--- Simple AI Agent starting in: {ctx.room.name} ---")

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    agent = Agent(
        instructions=(
            "You are a warm, caring AI companion for elderly Korean users.\n\n"
            "# CRITICAL RULE: Language\n"
            "- User speaks: Korean (한국어)\n"
            "- You MUST respond: ONLY in Korean (한국어) using respectful 존댓말\n"
            "- NEVER respond in English - ALWAYS Korean\n"
            "- Example correct: '안녕하세요, 어르신'\n"
            "- Example WRONG: 'Hello' or any English\n\n"
            "# Output rules\n"
            "- Use respectful Korean speech (존댓말) at all times\n"
            "- Keep responses brief: one to two sentences\n"
            "- Respond naturally to what they say\n"
            "- Be warm and caring in tone\n\n"
            "# Conversational flow\n"
            "- Listen more than you speak\n"
            "- Respond to their stories with empathy\n"
            "- Share relevant observations about wellbeing, meals, activities\n"
            "- Only ask questions when it naturally fits\n\n"
            "# Handling interruptions\n"
            "- If interrupted, stop and listen\n"
            "- Acknowledge gracefully: '네, 말씀하세요'\n\n"
            "# Topics\n"
            "- Daily activities and meals\n"
            "- Health and feelings\n"
            "- Family and memories\n"
            "- Weather and seasons"
        ),
        # ✅ Configure models IN THE AGENT (not session) for proper instruction binding
        stt=openai.STT(language="ko"),  # Korean speech-to-text
        llm=openai.LLM(
            model="gpt-3.5-turbo",
            temperature=0.7,  # Slightly lower for more consistent responses
        ),
        tts=openai.TTS(
            voice="alloy",
            speed=1.0,  # Normal speed (can increase to 1.1-1.25 for faster)
        ),
        vad=silero.VAD.load(
            min_speech_duration=0.1,  # Detect speech faster (default 0.25s)
            min_silence_duration=0.3,  # End speech faster after silence (default 0.5s)
        ),
        # Timing optimizations - REDUCE transcript delay
        allow_interruptions=True,
        min_endpointing_delay=0.5,  # REDUCED: Wait only 0.5s before responding (was 1.0s)
        max_endpointing_delay=2.0,  # REDUCED: Max wait 2s (was 8.0s) - elderly can pause but not too long
    )

    session = AgentSession(
        # Additional session-level settings
        min_interruption_duration=1.2,
        min_interruption_words=2,
        false_interruption_timeout=3.0,
        resume_false_interruption=True,
        discard_audio_if_uninterruptible=False,
    )

    await session.start(agent, room=ctx.room)

    # Greeting in Korean (not English!)
    session.say("안녕하세요, 어르신. 오늘 어떻게 지내셨어요?")

    print(f"--- Agent ready and listening! ---")


if __name__ == "__main__":
    print("=" * 50)
    print("SIMPLE VOICE ASSISTANT")
    print("Requires: OPENAI_API_KEY in .env")
    print("=" * 50)
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
