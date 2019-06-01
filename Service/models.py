from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # ForeignKey 다 대 일 관꼐 설정
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    pub_data = models.DateTimeField(auto_now_add=True, blank=True)
    body = models.TextField(default='SOME STRING')
    
    # like_user_set = 모델과 다 대 다 관계를 형성함.
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL, blank = True, related_name='like_user_set', through='Like')

    # get method 표현
    @property
    # 좋아요 갯수를 세는 함수
    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    service = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    class Meta:
        unique_together = (('user', 'service'))


class Comment(models.Model):
    service = models.ForeignKey('Post',on_delete=models.CASCADE, related_name='comments')
    comment_author = models.CharField(max_length = 10)
    comment_contents = models.TextField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)