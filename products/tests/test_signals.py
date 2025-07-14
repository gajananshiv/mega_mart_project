import pytest
import os
from django.conf import settings
from products.models import Product, ProductImage, Category
from django.core.files.uploadedfile import SimpleUploadedFile

@pytest.mark.django_db
def test_image_file_deleted_with_product_image():
    # Create required instances
    category = Category.objects.create(name="Electronics")
    product = Product.objects.create(
        name="Test Product",
        category=category,
        price=199.99,
        stock=5
    )

    # Create a fake image file
    image_content = b"dummy_image_data"
    image_file = SimpleUploadedFile("test.jpg", image_content, content_type="image/jpeg")

    product_image = ProductImage.objects.create(
        product=product,
        image=image_file
    )

    # Full file path
    image_path = product_image.image.path

    # Ensure file exists before delete
    assert os.path.exists(image_path)

    # Delete object (which triggers signal)
    product_image.delete()

    # Assert file is deleted
    assert not os.path.exists(image_path)
