
from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.capacity import can_reserve_room


app = FastAPI(
    title="XP Meeting Kata",
    description="Extreme Programming experiment",
    version="0.2.0",
)


class CapacityRequest(BaseModel):
    participants: int = Field(gt=0)
    capacity: int = Field(gt=0)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/meetings/validate-capacity")
def validate_capacity(
    payload: CapacityRequest
) -> dict[str, bool]:

    accepted = can_reserve_room(
        participants=payload.participants,
        capacity=payload.capacity,
    )

    return {"accepted": accepted}
