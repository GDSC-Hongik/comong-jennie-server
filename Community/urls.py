from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import grade,sub,prof,posts,post_detail
from .views import post_detail, grade_post ,sub_post , prof_post
app_name = "Community"

# router = DefaultRouter()
# router.register('', post, basename='post')  


# router url 종류 파악 필요

urlpatterns = [
    # path('', ) 메인화면 구인,전공, 즐겨찾기로 이동 가능하게 
    #path('<int:pk>/posts', include(router.urls),name= 'mainboard'),
    # path('<int:board_pk>/posts/',post_list.as_view(), name= 'post-list'),
    # path('<int:board_pk>/posts/<int:post_pk>/',post_deatil.as_view(), name= 'post-deatil'),
    # path('major/', grade_list ,name = 'get_grade'),
    path('major/<int:grade>/', grade_post, name ='grade-post'),
    path('major/<int:grade>/<str:sub>/',sub_post, name = 'sub-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>',prof_post,name = 'prof-post'),
    path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>',post_detail.as_view(),name = 'post-detail')
    # path('major/<int:grade>/<str:sub>/<str:profs>/<int:post_pk>/create',post_detail.as_view(),name = 'post-create')
]