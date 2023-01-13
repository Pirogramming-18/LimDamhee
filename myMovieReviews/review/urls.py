from django.urls import path
from . import views
from review.views import reviews_list, reviews_create, reviews_retrieve, rewviews_delete, reviews_update

urlpatterns = [
    path('', reviews_list),
    path("review/create", reviews_create),
    path('review/<int:pk>/', reviews_retrieve),
    path('review/<int:pk>/delete', rewviews_delete),
    path('review/<int:pk>/update', reviews_update),
]