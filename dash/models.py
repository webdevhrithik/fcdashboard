from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
      return self.name

class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    language = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', null=True)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.title