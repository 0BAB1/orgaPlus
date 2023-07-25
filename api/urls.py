from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    #Home page
    path("categories/", views.CategoryView.as_view(), name="categoryView"),
    path("tasks/", views.TaskView.as_view(), name="taskView")
]