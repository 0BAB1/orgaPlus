from rest_framework import serializers
from .models import Category, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
                    "id",
                    "category",
                    "description",
                    "date",
                    "finished",
                    "priority",
                )

class CategorySerializer(serializers.ModelSerializer):
    # tasks = TaskSerializer(many = True)

    class Meta:
        model = Category
        fields = ("id", "title")