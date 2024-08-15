'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import UserViewSet

# DRF 라우터 설정
# 뷰셋 등록, RESTful API 엔드포인트 자동 생성
router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("",views.index,name="index"),
    path("users/<int:user_id>/",views.ProfileView.as_view(),name="profile"),

    # 프로필 설정
    path("set-profile/",views.ProfileSetView.as_view(),name="profile-set"),
    # 프로필 수정
    path("edit-profile/",views.ProfileUpdateView.as_view(),name="profile-update"),
    
    # DRF 라우터 URL
    path('api/', include(router.urls)),
]
'''
from django.urls import path
from .views import RegistrationAPIview,LoginAPIview,UserRetrieveUpdateAPIview,resume_list

urlpatterns = [
    path('register/',RegistrationAPIview.as_view(),name="register"),
    path('login/',LoginAPIview.as_view(),name="login"),
    path('current/',UserRetrieveUpdateAPIview.as_view(),name="profile"),
    path('resumes/<int:pk>/',resume_list,name="resume"),
]