from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponseRedirect , JsonResponse
from django.urls import reverse
from .models import Post , Board
from .serializers import PostdetailSerializer ,PostlistSerializer ,BoardSerializer , Subserializer , Profserializer

## 코드 전반적으로 오류처리에 대한 부분 필요

# class post(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostdetailSerializer
"""

"""
class post_list(APIView):
    def get(self,request,board_pk):
        board = Board.objects.get(id = board_pk)
        posts = Post.objects.filter(board_pk=board_pk)
        serializer = PostlistSerializer(posts,many=True)
        return Response({'board name':str(board) ,'data':serializer.data})
    
    def post(self,request,board_pk):
        data = request.data
        data ['board_pk'] = board_pk
        serializer = PostdetailSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
            return HttpResponseRedirect(reverse('Community:post-list', kwargs={'board_pk': board_pk } ))
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# def post_detail(request,board_pk,post_pk):
#     post = Post.objects.get(board_pk=board_pk,id=post_pk)
#     serializer = PostdetailSerializer(post)
#     return Response(serializer.data)

class post_deatil(APIView): 
    def get_object(self,board_pk,post_pk):
        post = get_object_or_404(Post,board_pk=board_pk,id=post_pk)
        return post

    def get(self,request,board_pk,post_pk):
        post = self.get_object(board_pk,post_pk)
        serializer = PostdetailSerializer(post)
        return Response(serializer.data)
    
    def patch(self,request,board_pk,post_pk):
        post = self.get_object(board_pk,post_pk)
        serializer = PostdetailSerializer(post,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self,request,board_pk,post_pk):
        post = self.get_object(board_pk,post_pk)
        url = reverse('Community:post-list', kwargs={'board_pk': board_pk })
        post.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponseRedirect(url)
        return Response({'url': str(url) }, status=status.HTTP_204_NO_CONTENT) ###여기서 url이 전달되는지 프론트와 확인 필요

# post_list에서는 제목,작성자(+프로필),시간,태그만 보이도록(content 제외) 세부 기능 구현+해당 게시판에 맞는 게시물만 보이도록
# ModelViewset 조금 더 공부 필요


@api_view(['GET', 'POST'])
def grade_list(request):
    if request.method == 'GET' :
        board = Board.objects.values('grade').order_by('grade').distinct()    
        serializer = BoardSerializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method =='POST':
        return HttpResponseRedirect(reverse('Community:get_sub', kwargs={'grade' : request.data}))


@api_view(['GET', 'POST']) 
def sub_list(request,grade):
    if request.method == 'GET' :
        board = Board.objects.filter(grade = grade).values('sub').order_by('sub').distinct()
        serializer = Subserializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    elif request.method =='POST':
        return HttpResponseRedirect(reverse('Community:get_prof', kwargs={'grade': grade , 'sub' : request.data}))
    

@api_view(['GET', 'POST']) 
def prof_list(request,grade,sub):
    if request.method == 'GET' :
        board = Board.objects.filter(sub=sub).order_by('profs')
        serializer = Profserializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
     
    elif request.method =='POST':
        board=Board.objects.get(grade=grade,sub=sub,profs=request.data)
        return HttpResponseRedirect(reverse('Community:post-list', kwargs={'board_pk':board.id}))