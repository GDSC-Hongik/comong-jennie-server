from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import grade,sub,prof,posts,post_detail
from .views import post_detail,post_create,grade_post ,sub_post , prof_post , notice_view , join_post_list,join_post_detail,join_post_create
app_name = "Community"



urlpatterns = [
    # 전공 게시판
    path('major/<int:grade>/', grade_post, name ='grade-post'),
    path('major/<int:grade>/<str:sub>/',sub_post, name = 'sub-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>/',prof_post,name = 'prof-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>/',post_detail.as_view(), name = 'post-detail'),
    path('major/<int:grade>/<str:sub>/<str:profs>/create/', post_create.as_view() , name = 'post-create'),
    # 구인 게시판
    path('join/',join_post_list,name = 'join-post-list'),
    path('join/<int:post_pk>/',join_post_detail.as_view(),name = 'join-post-detail'),
    path('join/create/',join_post_create.as_view(),name = 'join -post-create'),
    
    # 학과 공지사항
    path('notice/',notice_view, name = 'notice')
    
]