import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    text = models.TextField(null=True)
    author = models.CharField(max_length=20)
    published_date = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.author} - published in {self.category}"
    
    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)