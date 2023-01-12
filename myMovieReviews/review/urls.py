from django.urls import path
from . import views
from review.views import reviews_list, reviews_create, reviews_retrieve

urlpatterns = [
    path('', reviews_list, name='reviews_list'),
    path("review/create", reviews_create),
    path('review/<int:pk>/', reviews_retrieve, name='reviews_retrieve'),

]