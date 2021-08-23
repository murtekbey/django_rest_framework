from rest_framework import serializers
from product.models import Comment, Product, Category
from django.utils.text import slugify


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ['product']
        read_only_fields = ['id', 'created_date', 'updated_date']


class ProductSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    def get_slug(self, instance):
        return slugify(instance.name)

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['category']
        read_only_fields = ['id', 'created_date', 'updated_date']


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    def get_slug(self, instance):
        return slugify(instance.name)

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id', 'created_date', 'updated_date']
