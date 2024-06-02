from django.urls import path

from common import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'search', views.ProductSearchViewSet, basename='product-search')


urlpatterns = [
    #category
    path('category/', views.CategoryListCreateView.as_view()),
    path('category/details/<int:id>/', views.CategoryListCreateView.as_view()),

    #product
    path('product/', views.ProductListCreateView.as_view()),
    path('product/details/<int:id>/', views.ProductDetailView)
]

urlpatterns += router.urls