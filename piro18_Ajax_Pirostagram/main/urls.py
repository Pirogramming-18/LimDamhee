from django.urls import path
from . import views
from django.contrib import admin

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('create-comment/', views.create_comment),
    path('delete-comment/', views.delete_comment),
]
