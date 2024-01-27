from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, verbose_name="Email Address")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='blog title')
    desc = models.TextField()
    article = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    thubnail = models.ImageField(upload_to="thunbnail", default="example.jpg")

    def __str__(self) -> str:
        return self.title
