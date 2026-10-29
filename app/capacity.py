
def can_reserve_room(
    participants: int,
    capacity: int
) -> bool:

    if participants <= 0:
        raise ValueError(
            "Le nombre de participants doit être positif"
        )

    if capacity <= 0:
        raise ValueError(
            "La capacité doit être positive"
        )

    if participants <= capacity:
        return True

    return False
