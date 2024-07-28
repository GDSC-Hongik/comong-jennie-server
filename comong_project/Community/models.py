from django.db import models
from User.models import User
# from .models import Board, HashTag
# Create your models here.


class Board(models.Model):
    grade = models.IntegerField()
    sub = models.CharField(max_length=30)
    profs = models.CharField(max_length=30)
    
    def __str__(self):
        return '{0}/{1}/{2}'.format(self.grade,self.sub,self.profs)
    
class HashTag(models.Model):
    tag = models.TextField()

    def __str__(self):
        return self.content

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author= models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    tag = models.ManyToManyField(HashTag,blank=True)
    dt_created = models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified",auto_now=True)
    # board = models.OneToOneField(Board )
    
    def __str__(self):
        return self.title

# class likes():
#     pass
# class comment():
#     pass




