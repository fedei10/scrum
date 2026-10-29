
import pytest

from app.capacity import can_reserve_room


@pytest.mark.parametrize(
    "participants,capacity,expected",
    [
        (5, 10, True),
        (10, 10, True),
        (12, 10, False),
    ],
)
def test_capacity(
    participants: int,
    capacity: int,
    expected: bool,
) -> None:

    assert can_reserve_room(
        participants,
        capacity
    ) is expected


@pytest.mark.parametrize(
    "participants,capacity",
    [
        (0, 10),
        (-1, 10),
        (5, 0),
        (5, -3),
    ],
)
def test_invalid_values(
    participants: int,
    capacity: int,
) -> None:

    with pytest.raises(ValueError):
        can_reserve_room(
            participants,
            capacity
        )
