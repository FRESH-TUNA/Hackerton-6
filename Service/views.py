from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from .models import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .utills import testReadAuth
# from django.utils.datastructures import MultiValueDictKeyError

@login_required
def home(request):
    postsPaginator = Paginator(Post.objects.all(), 5)
    
    # 다른 방법
    # try:
    #     currentPage = request.GET['page']
    # except MultiValueDictKeyError:
    #     currentPage = 1

    currentPage = request.GET.get('page', False)
    if currentPage == False:
        currentPage = 1

    posts = postsPaginator.get_page(currentPage)
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



def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = post.like_set.get_or_create(user = request.user)

    if not post_like_created:
        post_like.delete()
        return redirect('/testRead/' + str(post.id))
    return redirect('/testRead/' + str(post.id))


@testReadAuth.login_required
def comment(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
            # 만들어준 Comment model을 살펴보고 이에 해당되는 POST로 받은 부분을 넣어준다.
        Comment.objects.create(
            service = post_detail,
            comment_author=request.POST.get('comment_author'),
            comment_contents=request.POST.get('comment_contents'),
        )
        return redirect('/testRead/' + str(post_id))
# return render(request, 'testRead.html',{'testRead':details})
