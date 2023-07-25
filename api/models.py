from django.db import models

# Create your models here.
class Category(models.Model):
    """Taask category, just a title under which we store task. Meant to be a tem member's name"""
    title = models.CharField(max_length=50, default="Nouvelle cotégorie", unique=True)

class Task(models.Model):
    """a task is linked to a category, has a descrption (the only readable data btw) and annex data : date, priority and finished"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="Nouvelle tache")
    date = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)