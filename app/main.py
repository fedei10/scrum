"""Squelette FastAPI utilisé pour préparer l'expérimentation XP.

La logique de réservation n'est volontairement pas implémentée pendant
la semaine 1. Elle servira aux itérations comparative et TDD en semaine 2.
"""
from fastapi import FastAPI

app = FastAPI(
    title="XP Meeting Kata",
    description="Support pédagogique pour étudier Extreme Programming",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Point de contrôle minimal vérifié par le pipeline CI."""
    return {"status": "ok"}
