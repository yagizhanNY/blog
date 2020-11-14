from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_created=True, null=False)
    author = models.CharField(max_length=100, null=False)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
