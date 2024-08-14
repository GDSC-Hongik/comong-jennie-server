from django.db import models
from User.models import User
# from .models import Board, HashTag
# Create your models here.

class HashTag(models.Model):
    tags= (
        (0,'전공 과목'),
        (1,'프로젝트' ),
        (2, '대학원'),
        (3,'학부 연구생'),
        (4,'인턴'),
        (5, '구인'),
        (6,'백엔드'),
        (7,'프론트'),
    )
    
    tag = models.CharField(max_length=1,choices=tags)

    def __str__(self):
        return self.content

class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    author= models.CharField(max_length=15,null=True)     
    tag = models.ManyToManyField(HashTag,blank=True)
    
    dt_created = models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified",auto_now=True) 
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.title,self.author,self.dt_created)
    

class Sub_post(Post):
    grade = models.IntegerField(null=True)
    sub = models.CharField(max_length=30,null=True)
    profs = models.CharField(max_length=30,null=True)
    
class Join_post(Post):
    participants_num = models.IntegerField(null=True)
    current_num = models.IntegerField(null=True)
    
class Comment(models.Model):
    id = models.AutoField(primary_key=True,null=False,blank=False)
    sub_post = models.ForeignKey(Sub_post,null=False,blank=False,on_delete=models.CASCADE) # Post의 id와 Comment의 post는 동일값을 가짐
    user = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True,null=False,blank=False)
    comment = models.TextField()

    def __str__(self):
        return self.comment

class likes(models.Model):
    like = models.IntegerField(null=True,default=0)
    sub_post = models.ForeignKey(Sub_post,null=True,blank=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=False,on_delete=models.CASCADE)

class Notice(models.Model):
    title = models.CharField(max_length=100,null=True)
    content_url = models.URLField(max_length=500,null=True)
    
    def __str__(self):
        return self.title
    
class Scrap(models.Model):
    scrap_board = models.URLField(max_length=100,null=True)




