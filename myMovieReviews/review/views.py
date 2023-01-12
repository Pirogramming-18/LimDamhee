from django.shortcuts import render, redirect
from .models import Review
from django.http.request import HttpRequest

def reviews_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review_list.html', {"reviews": reviews})

def reviews_retrieve(request, pk, *args, **kwargs):
    review = Review.objects.all().get(id=pk)
    return render(request, "review/review_retrieve.html", {"review": review})

def reviews_create(request:HttpRequest, *args, **kwargs):
    if request.method == "REVIEW":
        Review.objects.create(
            title=request.REVIEW["title"],
            director=request.REVIEW["director"],
            character=request.REVIEW["character"],
            genre=request.REVIEW["genre"],
            star=request.REVIEW["star"],
            time=request.REVIEW["time"],
            content=request.REVIEW["content"],
        )
        return redirect("/")
    return render(request, "review/review_create.html")
