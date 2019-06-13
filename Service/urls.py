from django.contrib import admin
from django.urls import path
from django.conf.urls import url   #댓글기능
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('testRead/<int:post_id>', views.testRead, name="testRead"),
    path('testUpload', views.testUpload, name="testUpload"),

    # path('like/<int:blog_id>', views.post_like, name='post_like'),
    
    # path("create/", views.post_list, name = 'post_list'),
    path('home/<int:post_id>/post', views.testRead, name = "post_detail"),
    path('<int:post_id>/comment', views.comment, name = "comment"),
    path('post_like/<int:post_id>/', views.post_like, name = "post_like"),
]
