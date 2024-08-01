from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponseRedirect , JsonResponse , Http404
from django.urls import reverse
from .models import Post 
from .serializers import PostdetailSerializer ,GradePostlistSerializer,SubPostlistSerializer , ProfsPostlistSerializer

## 코드 전반적으로 오류처리에 대한 부분 필요


@api_view(['GET']) 
def grade_post(request,grade):
    if request.method == 'GET' :
        posts = Post.objects.filter(grade = grade).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        serializer = GradePostlistSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
        
    
@api_view(['GET']) 
def sub_post(request,grade,sub):
    if request.method == 'GET' :
        posts = Post.objects.filter(grade = grade, sub=sub).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        serializer = SubPostlistSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
     

@api_view(['GET']) 
def prof_post(request,grade,sub,profs):
    if request.method == 'GET' :
        posts = Post.objects.filter(grade = grade, sub=sub, profs = profs).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        serializer = ProfsPostlistSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    


class post_detail(APIView): 
    def get_object(self, post_pk):
        post = get_object_or_404(Post, id=post_pk)
        return post

    def get(self,request,grade,sub,profs,post_pk):
        post = self.get_object(post_pk)
        serializer = PostdetailSerializer(post)
        return Response(serializer.data)
    
    def patch(self,request,grade,sub,profs,post_pk):
        post = self.get_object(post_pk)
        serializer = PostdetailSerializer(post,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self,request,grade,sub,profs,post_pk):
        post = self.get_object(post_pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class post_create(APIView):
    def get(self,request,grade,sub,profs):
        return Response(status=status.HTTP_200_OK)
    
    def post(self,request,grade,sub,profs):
        data = request.data
        data ['grade'] = grade
        data ['sub'] = sub
        data ['profs'] = profs
        serializer = PostdetailSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
            # return HttpResponseRedirect(reverse('Community:post-list', kwargs={'board_pk': board_pk } ))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)