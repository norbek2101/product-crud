from common.models import Category, Product
from common.serializers import CategorySerializer, ProductSerializer

from rest_framework import generics, permissions, parsers


#Category
class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.MultiPartParser,)
    my_tags = ['Category']


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.MultiPartParser,)
    queryset = Category.objects.all()
    my_tags = ['Category']

#Product
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.MultiPartParser,)
    my_tags = ['Product']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = (parsers.MultiPartParser,)
    queryset = Product.objects.all()
    my_tags = ['Product']