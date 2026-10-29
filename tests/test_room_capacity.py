
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
def test_room_capacity(
    participants, capacity, expected
):
    assert can_reserve_room(
        participants, capacity
    ) is expected


@pytest.mark.parametrize(
    "participants,capacity",
    [
        (0, 10),
        (5, 0),
    ],
)
def test_invalid_capacity(participants, capacity):
    with pytest.raises(ValueError):
        can_reserve_room(participants, capacity)
