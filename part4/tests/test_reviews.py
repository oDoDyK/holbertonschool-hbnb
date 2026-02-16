def test_review_owner_only(client, token):
    place = client.post(
        "/api/v1/places",
        headers={"Authorization": f"Bearer {token}"},
        json={"name": "Place"}
    ).json

    review = client.post(
        f"/api/v1/places/{place['id']}/reviews",
        headers={"Authorization": f"Bearer {token}"},
        json={"text": "Nice"}
    )

    assert review.status_code == 201
