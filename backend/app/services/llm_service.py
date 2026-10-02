from __future__ import annotations

import os

from openai import OpenAI

from backend.app.config.settings import settings


class LLMService:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY) if settings.OPENAI_API_KEY and settings.OPENAI_API_KEY != "demo_key" else None
        self.model = settings.OPENAI_MODEL

    def chat(self, prompt: str, system_prompt: str | None = None) -> str:
        if self.client is None:
            return "LLM is unavailable in local demo mode, using deterministic fallback logic."

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt or "You are a grounded retail data-quality assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
        )
        return response.choices[0].message.content or ""

    def embed(self, text: str) -> list[float]:
        if self.client is None:
            return [0.0] * 1536

        response = self.client.embeddings.create(
            model=settings.OPENAI_EMBEDDING_MODEL,
            input=text,
        )
        return response.data[0].embedding
