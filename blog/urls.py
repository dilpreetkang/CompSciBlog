from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("todo/<int:pk>/", views.todo_index, name="todo_index"),
    path("about/", views.about_index, name="about_index"),
]
