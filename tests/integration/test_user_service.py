def test_users(client, setOneUser):
    response = client.get("/api/user")
    assert response.status_code == 200
    names = [(p["first_name"], p["last_name"]) for p in response.json()]
    assert ("john", "doe") in names

def test_empty_user(client):
    response = client.get("/api/user")
    assert response.status_code == 200
    assert response.json() == []