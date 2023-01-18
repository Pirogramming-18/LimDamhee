from django.shortcuts import render, redirect
from server.apps.posts.models import Post, Devtool
from django.http.request import HttpRequest

#게시글 파트
def posts_list(request:HttpRequest, *args, **kwargs):
    posts = Post.objects.all()

    #text = request.GET.get("text")
    #if text:
    #    posts = posts.filter(content__contains=text)
    
    context = {
        "posts" : posts,
    }

    return render(request, "posts/posts_list.html", {"posts":posts})

def posts_retrieve(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)

    return render(request, "posts/posts_retrieve.html", {"post": post})

def posts_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title=request.POST["title"],
            content=request.POST["content"],
            interest=request.POST["interest"],
            photo=request.FILES["photo"],
            devtool=request.POST["devtool"]
        )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")

def posts_update(request:HttpRequest, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title=request.POST["title"]
        post.content=request.POST["content"]
        post.interest=request.POST["interest"]
        post.photo=request.FILES.get("photo")
        post.devtool=request.POST["devtool"]
        post.save()
        return redirect(f"/posts/{post.id}")
    return render(request, "posts/posts_update.html", {"post":post})

##개발툴 파트

def dev_list(request:HttpRequest, *args, **kwargs):
    devs = Devtool.objects.all()

    return render(request, "posts/dev_list.html", {"devs":devs})

def dev_retrieve(request:HttpRequest, pk, *args, **kwargs):
    dev = Devtool.objects.get(id=pk)

    return render(request, "posts/dev_retrieve.html", {"dev": dev})

def dev_create(request:HttpRequest, *args, **kwargs):
    if request.method == "POST":
        Devtool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"]
        )
        return redirect("/devs")
    return render(request, "posts/dev_create.html")

def dev_update(request:HttpRequest, pk, *args, **kwargs):
    dev = Devtool.objects.get(id=pk)
    if request.method == "POST":
        dev.name=request.POST["name"]
        dev.content=request.POST["content"]
        dev.kind=request.POST["kind"]
        dev.save()
        return redirect(f"/devs/{dev.id}")
    return render(request, "posts/dev_update.html", {"dev":dev})

def dev_delete(request:HttpRequest, pk, *args, **kwargs):
    if request.method == "POST":
        dev = Devtool.objects.get(id=pk)
        dev.delete()
    return redirect("/devs")

#찜하기 기능
def show_important_post(request):
    posts = Post.objects.all()
    return render(request,'posts/star_postion.html',{'posts':posts})