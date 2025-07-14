import pytest
from products.models import Category

@pytest.mark.django_db
def test_category_str():
    cat = Category.objects.create(name="Electronics")
    assert str(cat) == "Electronics"
