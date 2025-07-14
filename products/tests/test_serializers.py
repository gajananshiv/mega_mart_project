# products/tests/test_serializers.py

import pytest
from products.serializers import ProductSerializer

@pytest.mark.django_db
def test_product_serializer_validation_error():
    # ✅ 'name' diya gaya taaki 'price' bhi validate ho
    payload = {
        "name": "Test Product",
        "price": -100,
        "stock": 5
    }

    serializer = ProductSerializer(data=payload)
    is_valid = serializer.is_valid()

    assert is_valid is False
    assert "price" in serializer.errors  # ✅ yeh ab pass hoga
