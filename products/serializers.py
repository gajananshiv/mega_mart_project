from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'is_active', 'created_at']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'is_active', 'created_at']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_featured', 'uploaded_at']




class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )
    brand_id = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(), write_only=True, source='brand'
    )
    price = serializers.DecimalField(max_digits=10, decimal_places=2,required=True)

    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'stock',
            'is_active', 'created_at', 'category','category_id', 'brand','brand_id', 'images'
        ]

    def validate_price(self, value):
        print("Debug: Price received ->", value)
        #import pdb; pdb.set_trace()
        if value <=0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_price(self,value):
        if value==100000:
            raise serializers.ValidationError("price not 100000")
        return value

# POST/PUT ke liye: create/update serializer with category & brand IDs
class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'stock',
            'is_active', 'category', 'brand'
        ]

   