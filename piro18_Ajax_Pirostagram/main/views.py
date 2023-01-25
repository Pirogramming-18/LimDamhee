from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    ctx = {
        'posts': posts,
        'comments':comments,
    }
    return render(request, 'main/post_list.html', ctx)

@csrf_exempt
def create_comment(request, *args, **kwargs):
    req = json.loads(request.body)
    text = req['text']  
    newComment = Comment(comment = text)
    newComment.save()
    return JsonResponse({'id': newComment.pk, 'text': newComment.comment})

@csrf_exempt
def delete_comment(request, *args, **kwargs):
    req = json.loads(request.body)
    id = req['id']
    Comment.objects.all().get(id=id).delete()
    return JsonResponse({'id': id})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)     # {id: 1, type: 'like'}
    post_id = req['id']     # 1
    button_type = req['type']   # 'like'

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        post.like += 1

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})   # {id: 1, type: 'like'}

