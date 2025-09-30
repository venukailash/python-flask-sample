def test_users(client, setOneUser):
    response = client.get("/api/user")
    assert response.status_code == 200
    names = [(p["first_name"], p["last_name"]) for p in response.json()]
    assert ("john", "doe") in names

def test_empty_user(client):
    response = client.get("/api/user")
    assert response.status_code == 200
    assert response.json() == []

def test_get_one_user(client, setOneUser):
    expected_response = {"id":1,"email": "v@b.com", "first_name":"john", "last_name":"doe"}
    response = client.get("/api/user/v@b.com")
    assert response.status_code == 200
    assert response.json() == expected_response

def test_get_one_empty_user(client):
    response = client.get("/api/user/nouser@missing.com")
    assert response.status_code == 404

def test_get_one_invalid_email(client):
    response = client.get("/api/user/invalid_email")
    assert response.status_code == 400