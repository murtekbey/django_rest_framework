from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

DEFAULT_STATUS = 'draft'

STATUS = [
    # sol kısım dbye yazılacak olan
    # sağ kısım kullanıcıya gözükecek
    # Page.objects.filter(status="draft").count()
    ('draft', 'Taslak'),
    ('published', 'Yayınlandı'),
    ('deleted', 'Silindi'),
]


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS, max_length=10,)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='category',
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=150)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10)
    is_home = models.BooleanField(default=False)
    content = models.TextField()
    image = models.ImageField(
        upload_to='product',
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk} - {self.name}"


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_owner')
    comment = models.TextField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
