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

    '''
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["user_tier"] = self.get_object().tier  # 티어 정보를 컨텍스트에 추가
        return context
    '''

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
