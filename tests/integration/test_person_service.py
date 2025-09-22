def test_people(client, setOnePerson):
    response = client.get("/api/people")
    assert response.status_code == 200
    names = [(p["fname"], p["lname"]) for p in response.json()]
    assert ("john", "doe") in names

def test_people_empty(client):
    response = client.get("/api/people")
    assert response.status_code == 200
    assert response.json() == []