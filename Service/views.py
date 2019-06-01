from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import Comment, Like, Post
from django.utils import timezone
from django.contrib.auth.models import User

def home(request):
    posts = Post.objects.all()
    return render(request, 'Service/main.html', {'posts': posts})

def testRead(request, post_id):
    # posts = Post.objects.all()
    post_detail = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        # 만들어준 Comment model을 살펴보고 이에 해당되는 POST로 받은 부분을 넣어준다.
        Comment.objects.create(
            service = post_detail,
            comment_author=request.POST.get('comment_author'),
            comment_contents=request.POST.get('comment_contents'),
        )
    return render(request, 'Service/testRead.html', {'post_detail': post_detail})

def testUpload(request):
    if request.method == "GET":
        return render(request, 'Service/testUpload.html')
    else:
        post = Post()
        post.author = request.user
        post.image = request.FILES['image']
        post.pub_data = timezone.datetime.now()
        post.body = request.POST['body']
        post.save()

        return redirect('testRead/' + str(post.id))


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = post.like_set.get_or_create(user = request.user)

    if not post_like_created:
        post_like.delete()
        return redirect('/testRead/' + str(post.id))
    return redirect('/testRead/' + str(post.id))


 # detail 함수에서 해당 detail(blog id)의 comment 객체 생성을 추가해준다.
def comment(request, comments_id):
    post_detail = get_object_or_404(Comment, pk= comments_id)
    if request.method == "POST":
            # 만들어준 Comment model을 살펴보고 이에 해당되는 POST로 받은 부분을 넣어준다.
            Comment.objects.create(
                blog = comments,
                comment_author=request.POST.get('comment_author'),
                comment_contents=request.POST.get('comment_contents'),
            )
            return redirect('/blog/'+str(details.id))
    return render(request, 'testRead.html',{'testRead':details})
