from django.shortcuts import render, reverse, redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage

def testRead(request):
    posts = Post.objects.all()
    return render(request, 'Service/testRead.html', {'posts': posts})

def testUpload(request):
    if request.method == "GET":
        return render(request, 'Service/testUpload.html')
    else:
        # myfile = request.FILES['image']
        # fs = FileSystemStorage()
        # filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        #post = Post(image=uploaded_file_url)
        postForm = PostForm(request.POST, request.FILES)
        postForm.save()
        return redirect('testRead')

