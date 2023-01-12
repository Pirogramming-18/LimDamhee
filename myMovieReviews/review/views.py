from django.shortcuts import render, redirect
from .models import Review
from django.http.request import HttpRequest

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_list.html', {"reviews": reviews})

def reviews_retrieve(request, pk, *args, **kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request, "review/review_retrieve.html", {"review": review})
