from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from django.http import HttpResponseRedirect , JsonResponse , Http404
from django.urls import reverse

from .models import Notice ,Sub_post,Join_post,Scrap
from .serializers import PostdetailSerializer ,GradePostlistSerializer,SubPostlistSerializer , ProfsPostlistSerializer, NoticelistSerializer , JoinpostdetailSerializer,JoinpostlistSerializer , ScrapSerializer


### 메인 화면

# 컴퓨터 공학과 공지사항을 보여주며 각 게시판의 URL을 제공.
# 즐겨찾기 추가 구현 완료.

@api_view(['GET'])
def main_view(request):
    notice = Notice.objects.all()
    serializer = NoticelistSerializer(notice, many=True)
    
    scraps_board = Scrap.objects.all()
    Scrapserializers = ScrapSerializer(scraps_board,many=True)
    return Response({'major_board' : reverse('Community:majorboard-view'),
                     'join_board' : reverse('Community:join-post-list'),
                     'Scrapped' : Scrapserializers.data,
                     'notice' : serializer.data},
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def majorboard_view(request):
    return Response(status=status.HTTP_200_OK )



### 전공게시판 

# 학년만 필터링된 게시물 List GET.
# 게시물 id, 제목, 과목명, 교수명, 생성일을 보여줌.
# 생성 최신일 순서로 정렬함.
# 검색 기능: 제목과 내용에서 해당 내용을 포함하는지 판단함.

class grade_post(ListAPIView):
    def get_queryset(self):
        grade = self.kwargs['grade']
        posts = Sub_post.objects.filter(grade = grade).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        return posts
    
    serializer_class = GradePostlistSerializer
    filter_backends=[SearchFilter]
    search_fields = ['title', 'content']
    
        
        
# 학년,과목명이 필터링된 게시물 List GET.
# 게시물 id, 제목, 교수명, 생성일을 보여줌.
# 생성 최신일 순서로 정렬함.
# 검색 기능: 제목과 내용에서 해당 내용을 포함하는지 판단함.

class sub_post(ListAPIView):
    def get_queryset(self):
        grade = self.kwargs['grade']
        sub = self.kwargs['sub']
        posts = Sub_post.objects.filter(grade = grade,sub = sub).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        return posts
    
    serializer_class = SubPostlistSerializer
    filter_backends=[SearchFilter]
    search_fields = ['title', 'content']
    
    
# 학년, 과목명, 교수명까지 모두 필터링된 게시물 List GET.
# 게시물 id, 제목, 생성일을 보여줌.
# 생성 최신일 순서로 정렬함.
# 검색 기능: 제목과 내용에서 해당 내용을 포함하는지 판단함.

class prof_post(ListAPIView):
    
    def get_queryset(self):
        grade = self.kwargs['grade']
        sub = self.kwargs['sub']
        profs = self.kwargs['profs']
        posts = Sub_post.objects.filter(grade = grade, sub = sub, profs = profs).order_by('-dt_created')
        if not posts:
            raise Http404(" Thers no data ")
        return posts
    serializer_class = ProfsPostlistSerializer
    filter_backends=[SearchFilter]
    search_fields = ['title', 'content']
    
### 즐겨찾기
# prof-post url뒤에 scrap을 이어 붙임.
# 해당 URL로 Post요청시 해당 Board의 url을 Scrap모델에 저장함.
# 중복되는 즐겨찾기 URL 있을 시 저장하지 않음 

class scrap_board(APIView):
    def get(self,request,grade,sub,profs):
        return Response(status=status.HTTP_200_OK)
    
    def post (self,request,grade,sub,profs):
        url = reverse('Community:prof-post', kwargs={'grade':grade,'sub':sub,'profs':profs})
        try :  
            board=Scrap.objects.get(scrap_board=url)
        except Scrap.DoesNotExist:
            Scrap.objects.create(scrap_board=url).save()
        return Response({'scrapped': url},status=status.HTTP_201_CREATED)
       
    
   
    
    
    

# 특정 게시물을 조회,수정,삭제.

class post_detail(APIView): 
    # 앞에서 전달받은 grade, sub, profs 인수를 통해 해당하는 게시물을 찾음(없다면 404)
    def get_object(self,grade,sub,profs,post_pk):
        post = get_object_or_404(Sub_post, grade = grade, sub = sub, profs = profs, id=post_pk)
        return post
    # 게시물 정보를 보여줌
    def get(self,request,grade,sub,profs,post_pk):
        post = self.get_object(grade,sub,profs,post_pk)
        serializer = PostdetailSerializer(post)
        return Response(serializer.data)
    # 게시물 수정 기능
    def patch(self,request,grade,sub,profs,post_pk):
        post = self.get_object(grade,sub,profs,post_pk)
        serializer = PostdetailSerializer(post,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    # 게시물 삭제 
    def delete(self,request,grade,sub,profs,post_pk):
        post = self.get_object(grade,sub,profs,post_pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# 게시물을 생성하려면 grade,sub,profs를 Front에서 전달받음.
# 'major/<int:grade>/<str:sub>/<str:profs>/create/'로 연결. 
# 해당 URL에서 인수들을 전달받아 생성하려는 게시물의 grade,sub,profs 필드에 저장함.

class post_create(APIView):
    # 아무 정보 없는 화면
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


###구인 게시판

@api_view(['GET'])
def join_post_list(request):
    if request.method == 'GET' :
        posts = Join_post.objects.all().order_by('-dt_created')
        serializers = JoinpostlistSerializer(posts, many=True)
        return Response(serializers.data,status= status.HTTP_200_OK)
    
class join_post_detail(APIView):
    def get_object(self,post_pk):
        post = get_object_or_404(Join_post, id=post_pk)
        return post
    # 게시물 정보 
    def get(self,request,post_pk):
        post = self.get_object(post_pk)
        serializer = JoinpostdetailSerializer(post)
        return Response(serializer.data)
    # 게시물 수정 기능
    def patch(self,request,post_pk):
        post = self.get_object(post_pk)
        serializer = JoinpostdetailSerializer(post,data=request.data,partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    # 게시물 삭제 
    def delete(self,request,post_pk):
        post = self.get_object(post_pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class join_post_create(APIView):
    def get(self,request):
        return Response(status= status.HTTP_200_OK)
    def post(self,request):
        data = request.data
        serializer = JoinpostdetailSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    




    
        