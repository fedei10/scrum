
def _require_positive(
    value: int,
    name: str
) -> None:
    """Vérifie qu'une valeur est positive."""

    if value <= 0:
        raise ValueError(
            f"{name} doit être strictement positif"
        )


def can_reserve_room(
    participants: int,
    capacity: int
) -> bool:
    """Vérifie la capacité d'une salle."""

    _require_positive(
        participants,
        "participants"
    )

    _require_positive(
        capacity,
        "capacity"
    )

    return participants <= capacity
