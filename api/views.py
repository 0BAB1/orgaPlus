from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

# Create your views here.*
class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer