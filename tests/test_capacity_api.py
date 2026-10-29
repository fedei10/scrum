
import pytest

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


@pytest.mark.parametrize(
    "participants,capacity,expected",
    [
        (5, 10, True),
        (10, 10, True),
        (12, 10, False),
    ],
)
def test_validate_capacity_endpoint(
    participants: int,
    capacity: int,
    expected: bool,
) -> None:

    response = client.post(
        "/meetings/validate-capacity",
        json={
            "participants": participants,
            "capacity": capacity,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "accepted": expected
    }


@pytest.mark.parametrize(
    "participants,capacity",
    [
        (0, 10),
        (5, 0),
    ],
)
def test_validate_capacity_rejects_invalid_input(
    participants: int,
    capacity: int,
) -> None:

    response = client.post(
        "/meetings/validate-capacity",
        json={
            "participants": participants,
            "capacity": capacity,
        },
    )

    assert response.status_code == 422
