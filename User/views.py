'''
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from rest_framework import viewsets
from .models import User
from .forms import ProfileForm
from .serializers import UserSerializer
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from django.shortcuts import render
from django.views.generic import DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# DRF 뷰셋
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 기존 Django 뷰
def index(request):
    return render(request, "User/index.html")

# 프로필 조회 -> DetailView 상속
class ProfileView(DetailView):
    model = User
    template_name = "User/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["user_tier"] = self.get_object().tier  # 티어 정보를 컨텍스트에 추가
        return context
    

# 프로필 설정 -> UpdateView 상속
class ProfileSetView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "User/profile_set_form.html"

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("index")
    
# 프로필 수정
class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "User/profile_update_form.html"

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile",kwargs={'user_id':self.request.user.id})

 
class CustomPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    def get_success_url(self):
        return reverse("profile",kwargs={'user_id':self.request.user.id})
'''
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from .serializers import RegistrationSerializer,LoginSerializer,UserSerializer,ResumeSerializer
from .renderers import UserJSONRenderer

from .models import User,Resume

# 회원가입
class RegistrationAPIview(APIView):
    permission_classes = (AllowAny,) # 회원가입은 누구나 가능
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)
    
    

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True) # 유효성 검사 
        serializer.save() # db에 저장
        
        return Response({
            'user': serializer.data,
            #'message': '회원가입이 완료되었습니다.',
            #'next': "login"  # 회원가입 후 로그인 페이지로 이동
        }, status=status.HTTP_201_CREATED)

# 로그인
class LoginAPIview(APIView):
    permission_classes = (AllowAny,) # 로그인도 누구나 가능
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)
    

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True) # 유효성 검사
           
        return Response({
            'user': serializer.data,
            #'message': '로그인이 완료되었습니다.',
            #'next': "profile"  # 로그인 후 프로필 수정 페이지로 이동
        }, status=status.HTTP_200_OK)

# 프로필 수정
class UserRetrieveUpdateAPIview(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,) # 인증된 사용자(=로그인한 사용자)만 접근
    serializer_class = UserSerializer
    renderer_classes = (UserJSONRenderer,)

    def get(self,request,*args,**kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data,status.HTTP_200_OK) # 유효성 검사 X, db에 저장 X / 단순히 user객체를 client에게 보내줌

    # 부분 업데이트(partial=True로 설정)
    def patch(self,request,*args,**kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(
            request.user,data=serializer_data,partial=True
        )   # 업데이트 : serializer_data(수정된 사항/validated_data)을 request.user(요청한 사용자 정보/instance)에 넣음
        
        serializer.is_valid(raise_exception=True) # 유효성 검사 
        serializer.save() # db에 저장
        
        return Response({
            'user': serializer.data,
            #'message': '프로필 수정이 완료되었습니다.',
            #'next': "home"  # 프로필 수정 후 로그인 페이지로 이동
        }, status=status.HTTP_200_OK)
        
# 이력서
@api_view(['GET', 'POST','PATCH','DELETE'])
def resume_list(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'GET':
        resumes = Resume.objects.filter(user=user)
        serializer = ResumeSerializer(resumes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        # 이력서 ID를 URL에서 가져옴
        resume_id = request.data.get('resume_id')  # 요청 데이터에서 resume_id를 가져옴
        resume = get_object_or_404(Resume, id=resume_id, user=user)

        serializer = ResumeSerializer(resume, data=request.data, partial=True)  # partial=True로 부분 업데이트 허용

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # 이력서 ID를 URL에서 가져옴
        resume_id = request.data.get('resume_id')  #  요청 데이터에서 resume_id를 가져옴
        resume = get_object_or_404(Resume, id=resume_id, user=user)

        resume.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

