from django.urls import path
from product.api import views as api_views

urlpatterns = [
    path('categories/', api_views.CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>', api_views.CategoryDetailAPIView.as_view(), name='category-detail'),

    path('categories/<int:category_pk>/add_product', api_views.ProductCreateAPIView.as_view(), name='add-product'),
    path('products/<int:pk>', api_views.ProductDetailAPIView.as_view(), name='product-detail'),

    path('products/<int:product_pk>/add_comment', api_views.CommentCreateAPIView.as_view(), name='add-comment'),
    path('comments/<int:pk>', api_views.CommentDetailAPIView.as_view(), name='comment-detail')
]