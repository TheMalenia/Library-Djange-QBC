from django.db import models

# Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish_date = models.DateField()
    # author = models.ForeignKey(Author, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    description = models.TextField(default="")
