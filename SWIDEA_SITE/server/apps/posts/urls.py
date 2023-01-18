from django.urls import path
from . import views

app_name = "posts"

urlpatterns= [
    path("", views.posts_list, name="list"),
    path("posts/create", views.posts_create, name="create"),
    path("posts/<int:pk>", views.posts_retrieve, name="retrieve"),
    path("posts/<int:pk>/update", views.posts_update, name="update"),
    path("posts/<int:pk>/delete", views.posts_delete, name="delete"),

    path("devs", views.dev_list, name="dev_list"),
    path("devs/dev_create", views.dev_create, name="dev_create"),
    path("devs/<int:pk>", views.dev_retrieve, name="dev_retrieve"),
    path("devs/<int:pk>/update", views.dev_update, name="dev_update"),
    path("devs/<int:pk>/delete", views.dev_delete, name="dev_delete")
]