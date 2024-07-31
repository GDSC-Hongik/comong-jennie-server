from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import grade,sub,prof,posts,post_detail
from .views import grade_list , sub_list , prof_list ,post_deatil, post_list
app_name = "Community"

# router = DefaultRouter()
# router.register('', post, basename='post')  


# router url 종류 파악 필요

urlpatterns = [
    # path('', ) 메인화면 구인,전공, 즐겨찾기로 이동 가능하게 
    #path('<int:pk>/posts', include(router.urls),name= 'mainboard'),
    path('<int:board_pk>/posts/',post_list.as_view(), name= 'post-list'),
    path('<int:board_pk>/posts/<int:post_pk>/',post_deatil.as_view(), name= 'post-deatil'),
    path('major/', grade_list ,name = 'get_grade'),
    path('major/<int:grade>/', sub_list, name ='get_sub'),
    path('major/<int:grade>/<str:sub>/', prof_list, name = 'get_prof'),
]