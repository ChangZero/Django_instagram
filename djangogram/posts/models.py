from ast import AugStore
from email.mime import image
from tkinter.tix import Tree
from venv import create
from django.db import models
from djangogram.users import models as user_model

#생성 및 업데이트 시간 클래스 생성 각 클래스에 상속시켜 사용할수 있도록함
class TimeStamedModels(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        
        
class Post(TimeStamedModels):
    author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_naem = 'post_author')
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name ='post_image_likes')
    
    
class Comment(TimeStamedModels):
    author = models.ForeignKey(
        user_model.User, 
        null=True, 
        on_delete=models.CASCADE, 
        related_naem = 'post_author')
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post'
    )
    contents = models.TextField(blank=True)