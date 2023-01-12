from django.urls import path
from . import views
from review.views import reviews_list, reviews_retrieve

urlpatterns = [
    path('', views.reviews_list, name='reviews_list'),
    path('review/<int:pk>/', views.reviews_retrieve, name='reviews_retrieve'),

]