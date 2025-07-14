from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer, ProductCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated,AllowAny

import pdb

# ✅ List and Create Products
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'brand']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'created_at']

    '''def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateUpdateSerializer
        return ProductSerializer'''
    def create(self, request, *args, **kwargs):
        print("DEBUG: Incoming product POST request")
        #pdb.set_trace()  # 👈 Ye execution yaha pause hoga
        print("DEBUG: Data =>", request.data)
        return super().create(request, *args, **kwargs)


# ✅ Retrieve, Update, Delete Product by Slug
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductCreateUpdateSerializer
        return ProductSerializer
