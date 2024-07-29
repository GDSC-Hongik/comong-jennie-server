from django.shortcuts import render,redirect

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post , Board
from .serializers import PostdetailSerializer , BoardSerializer , Subserializer , Profserializer


# @api_view(['GET'])
# def post_list(request):
#     posts=Post.objects.all()
#     serializer=PostlistSerializer(posts,many=True)
#     return Response(serializer.data, status=200)


# @api_view(['GET'])
# def post_deatil(request,pk):
#     posts_detail=Post.objects.get(id=pk)
#     serializer=PostdetailSerializer(posts_detail) # post object is not iterable
#     return Response(serializer.data, status=200)


class post(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostdetailSerializer
    
# post_list에서는 제목,작성자(+프로필),시간,태그만 보이도록(content 제외) 세부 기능 구현+해당 게시판에 맞는 게시물만 보이도록
# ModelViewset 조금 더 공부 필요

@api_view(['GET', 'POST'])
def grade_list(request):
    if request.method == 'GET' :
        board = Board.objects.values('grade').distinct()    
        serializer = BoardSerializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method =='POST':
        return HttpResponseRedirect(reverse('Community:get_sub', kwargs={'grade' : request.data}))

@api_view(['GET', 'POST']) 
def sub_list(request,grade):
    if request.method == 'GET' :
        board = Board.objects.filter(grade = grade).values('sub').distinct()
        serializer = Subserializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method =='POST':
        return HttpResponseRedirect(reverse('Community:get_prof', kwargs={'grade': grade , 'sub' : request.data}))
    

@api_view(['GET', 'POST']) 
def prof_list(request,grade,sub):
    if request.method == 'GET' :
        board = Board.objects.filter(sub=sub)
        serializer = Profserializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
     
    elif request.method =='POST':
        board=Board.objects.get(grade=grade,sub=sub,profs=request.data)
        return HttpResponseRedirect(reverse('Community:main_board', kwargs={'grade': grade , 'sub' : sub, 'prof':request.data}))
                                            ##여기서 mainview를 찾지 못 함