import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from products.models import Category

@pytest.mark.django_db
def test_create_product_api():
    client = APIClient()

    # Step 1: create a category
    category = Category.objects.create(name="Gadgets")

    # Step 2: prepare payload
    payload = {
        "name": "Smart Watch1",
        "price": "4999.00",
        "stock": 20,
        "category": category.id,
        "is_active": True
    }

    # Step 3: API call
    url = reverse("product-list-create")  # DRF router name
    response = client.post(url, payload, format="json")

    # Step 4: assert result
    assert response.status_code == 201
    assert response.data["name"] == "Smart Watch"
