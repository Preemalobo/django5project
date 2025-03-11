import pytest
from rest_framework import status

@pytest.mark.django_db
def test_user_registration(client):
    """Test user can register successfully"""
    payload = {
    "email": "newuser@example.com",
    "password": "newpassword123",
    "username": "newuser"  # ✅ Add this if required
}

    response = client.post("/api/users/register/", payload, content_type="application/json")

    # Debug output
    print("Response Status Code:", response.status_code)
    print("Response Data:", response.data)  # 👀 Print error details

    assert response.status_code == status.HTTP_201_CREATED
