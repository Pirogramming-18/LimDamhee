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
    if request.method == "POST":
        Review.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            director=request.POST["director"],
            character=request.POST["character"],
            genre=request.POST["genre"],
            star=request.POST["star"],
            time=request.POST["time"],
            content=request.POST["content"],
        )
        return redirect("/")
    return render(request, "review/review_create.html")


def rewviews_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/")

def reviews_update(request, pk, *args, **kwargs):
    review = Review.objects.get(id=pk)

    if request.method == "POST":
        review.title = request.POST["title"]
        review.year=request.POST["year"]
        review.director=request.POST["director"]
        review.character=request.POST["character"]
        review.genre=request.POST["genre"]
        review.star=request.POST["star"]
        review.time=request.POST["time"]
        review.content=request.POST["content"]      
        review.save()
        return redirect(f"/review/{review.id}")

    return render(request, "review/review_update.html", {"review": review})