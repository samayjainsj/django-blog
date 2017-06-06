from django.db import models
from simple_history.models import HistoricalRecords
from django import forms
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    history = HistoricalRecords()


class Post(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Date Published')
    history = HistoricalRecords()
