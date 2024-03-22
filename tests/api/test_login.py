import pytest
from async_asgi_testclient import TestClient

@pytest.mark.asyncio
async def test_success(client: TestClient) -> None:
    resp = await client.post(
        "/login",
        json={
            "email": "phucbv@example.com",
            "password": "123456",
        },
    )
    resp_json = resp.json()

    assert resp_json['code'] == "000"
    assert resp_json["message"] == "success"
    assert resp_json["data"]["access_token"] is not None

@pytest.mark.asyncio
async def test_wrong_email(client: TestClient) -> None:
    resp = await client.post(
        "/login",
        json={
            "email": "phucbv1@example.com",
            "password": "1234567",
        },
    )
    resp_json = resp.json()

    assert resp_json['detail'] == "Incorrect email or password"
