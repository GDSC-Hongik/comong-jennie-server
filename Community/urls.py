from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import post_detail,post_create,grade_post ,majorboard_view,sub_post , prof_post , main_view , join_post_list,join_post_detail,join_post_create,scrap_board,comment_detail,post_likes,join_post_update
app_name = "Community"



urlpatterns = [
    # 메인 화면(공지사항, 각 게시판 이동 경로)
    path('',main_view, name = 'main'),
    
    # 전공 게시판
    path('major/',majorboard_view.as_view(), name = 'majorboard-view'),
    path('major/<int:grade>/', grade_post.as_view(), name= 'grade-post'),
    path('major/<int:grade>/<str:sub>/',sub_post.as_view(), name = 'sub-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>/',prof_post.as_view(),name = 'prof-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>/scrap',scrap_board.as_view(),name = 'scrap-board'),
    path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>/',post_detail.as_view(), name = 'post-detail'),
    path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>/likes',post_likes.as_view(), name = 'post-likes'),
    path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>/<int:comment_pk>',comment_detail.as_view(), name = 'comment-detail'),
    path('major/<int:grade>/<str:sub>/<str:profs>/create/', post_create.as_view() , name = 'post-create'),
    
    # 구인 게시판
    path('join/',join_post_list, name = 'join-post-list'),
    path('join/<int:post_pk>/',join_post_detail.as_view(),name = 'join-post-detail'),
    path('join/<int:post_pk>/update',join_post_update.as_view(),name = 'join-post-update'),
    path('join/create/',join_post_create.as_view(),name = 'join -post-create'),

]