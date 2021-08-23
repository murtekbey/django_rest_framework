from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework import permissions

from product.api.serializers import CommentSerializer, ProductSerializer, CategorySerializer
from product.models import Category, Comment, Product
from product.api.permissions import IsAdminUserOrReadOnly, IsCommentOwnerOrReadOnly


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        category_pk = self.kwargs.get('category_pk')
        category = get_object_or_404(Category, pk=category_pk)
        serializer.save(category=category)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()  # gerek var mı?
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        product_pk = self.kwargs.get('product_pk')
        product = get_object_or_404(Product, pk=product_pk)
        user = self.request.user
        comments = Comment.objects.filter(product=product, comment_owner=user)
        if comments.exists():
            raise ValidationError('Bu ürüne daha önce yorum yapmışsınız.')
        serializer.save(product=product, comment_owner=user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCommentOwnerOrReadOnly]