from django.db import models
from User.models import User
# from .models import Board, HashTag
# Create your models here.





class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    author= models.CharField(max_length=15,null=True)     
    tag = models.CharField(max_length=15,null=True)
    
    dt_created = models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified",auto_now=True) 
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return '{0}/{1}/{2}/({4})'.format(self.title,self.author,self.dt_created, self.id)

class Sub_post(Post):
    grade = models.IntegerField(null=True)
    sub = models.CharField(max_length=30,null=True)
    profs = models.CharField(max_length=30,null=True)
    
class Join_post(Post):
    participants_num = models.IntegerField(null=True)
    current_num = models.IntegerField(null=True)

# class likes():
#     pass

# class comment():
#     pass

    
class HashTag(models.Model):
    tag = models.TextField()

    def __str__(self):
        return self.content

class Notice(models.Model):
    title = models.CharField(max_length=100,null=True)
    content_url = models.URLField(max_length=500,null=True)
    
    def __str__(self):
        return self.title



