from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.http import HttpResponseRedirect , JsonResponse
from django.urls import reverse
from .models import Post 
from .serializers import PostdetailSerializer ,GradePostlistSerializer,SubPostlistSerializer , ProfsPostlistSerializer

## 코드 전반적으로 오류처리에 대한 부분 필요

# class post(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostdetailSerializer
"""

"""
# class post_list(APIView):
#     def get(self,request,board_pk):
#         board = Board.objects.get(id = board_pk)
#         posts = Post.objects.filter(board_pk=board_pk)
#         serializer = PostlistSerializer(posts,many=True)
#         return Response({'board name':str(board) ,'data':serializer.data})
    
#     def post(self,request,board_pk):
#         data = request.data
#         data ['board_pk'] = board_pk
#         serializer = PostdetailSerializer(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # return Response(serializer.data,status=status.HTTP_201_CREATED)
#             return HttpResponseRedirect(reverse('Community:post-list', kwargs={'board_pk': board_pk } ))
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# def post_detail(request,board_pk,post_pk):
#     post = Post.objects.get(board_pk=board_pk,id=post_pk)
#     serializer = PostdetailSerializer(post)
#     return Response(serializer.data)

class post_detail(APIView): 
    def get_object(self,grade,sub,profs,post_pk):
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


@api_view(['GET']) 
def grade_post(request,grade):
    if request.method == 'GET' :
        posts = Post.objects.filter(grade = grade).order_by('dt_created')
        serializer = GradePostlistSerializer(posts, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
@api_view(['GET']) 
def sub_post(request,grade,sub):
    if request.method == 'GET' :
        board = Post.objects.filter(grade = grade, sub=sub).order_by('dt_created')
        serializer = SubPostlistSerializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)
     

@api_view(['GET']) 
def prof_post(request,grade,sub,profs):
    if request.method == 'GET' :
        board = Post.objects.filter(grade = grade, sub=sub, profs = profs).order_by('dt_created')
        serializer = ProfsPostlistSerializer(board, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)