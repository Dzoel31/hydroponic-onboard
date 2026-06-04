from pathlib import Path
import sys
from uuid import uuid7

from fastapi.testclient import TestClient


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import app
from utils.deps import get_session


client = TestClient(app)


class FakeScalarResult:
    def __init__(self, items: list[object]):
        self.items = items

    def all(self) -> list[object]:
        return self.items


class FakeExecuteResult:
    def __init__(self, items: list[object]):
        self.items = items

    def scalars(self) -> FakeScalarResult:
        return FakeScalarResult(self.items)


class FakeSession:
    def __init__(self) -> None:
        from models import Hydroponic

        self.items = [
            Hydroponic(
                id=uuid7(),
                moisture=70,
                temperature=26.0,
                humidity=65.0,
                ph=6.0,
                ec=1.2,
            ),
            Hydroponic(
                id=uuid7(),
                moisture=75,
                temperature=27.0,
                humidity=68.0,
                ph=6.3,
                ec=1.4,
            ),
        ]

    def add(self, item: object) -> None:
        item.id = uuid7()
        self.items.append(item)

    async def commit(self) -> None:
        pass

    async def refresh(self, item: object) -> None:
        pass

    async def execute(self, statement: object) -> FakeExecuteResult:
        return FakeExecuteResult(self.items)


async def override_get_session() -> FakeSession:
    return FakeSession()


app.dependency_overrides[get_session] = override_get_session


def test_list_hydroponic_data() -> None:
    response = client.get("/hydroponics")

    assert response.status_code == 200
    body = response.json()
    assert body["total"] >= 2
    assert isinstance(body["data"], list)


def test_create_hydroponic_data() -> None:
    payload = {
        "moisture": 80,
        "temperature": 27.1,
        "humidity": 67.5,
        "ph": 6.1,
        "ec": 1.45,
    }

    response = client.post("/hydroponics", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["moisture"] == payload["moisture"]
    assert body["temperature"] == payload["temperature"]
