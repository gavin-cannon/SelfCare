from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tasks/", views.taskList, name="tasks"),
    path("create/", views.createTask, name="create"),
    path('create/', views.create_self_care_item, name='create_self_care_item'),
]