from common.models import Category, Product
from common.serializers import CategorySerializer, ProductSerializer
from common.elasticsearch import ProductDocument

from rest_framework import generics, permissions, parsers

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)



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


#ElasticSearch
class ProductSearchViewSet(DocumentViewSet):
    document = ProductDocument
    serializer_class = ProductSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = ('name', 'description',)
    my_tags = ['ElasticSearch']