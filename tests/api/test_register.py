import pytest
from async_asgi_testclient import TestClient
from faker import Faker
fake = Faker()

@pytest.mark.asyncio
async def test_success(client: TestClient) -> None:
    fake_email = fake.email()
    resp = await client.post(
        "/register",
        json={
            "email": fake_email,
            "password": "123456",
            "full_name": "phuc"
        },
    )
    resp_json = resp.json()

    print("resp_json",resp_json)

    assert resp_json['code'] == "000"
    assert resp_json["message"] == "success"
    assert resp_json["data"]["id"] is not None

@pytest.mark.asyncio
async def test_email_taken(client: TestClient)-> None:
    resp = await client.post(
        "/register",
        json={
            "email": "phucbv@example.com",
            "password": "123456",
            "full_name": "phuc"
        },
    )
    resp_json = resp.json()

    assert resp_json['code'] == "400"
    assert resp_json["message"] == "Email already exists"
    assert resp_json["data"] == None
