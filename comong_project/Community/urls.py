from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import grade,sub,prof,posts,post_detail
from .views import post ,grade_list , sub_list , prof_list
app_name = "Community"

router = DefaultRouter()
router.register('', post)  

# router url 종류 파악 필요

urlpatterns = [
    # path('', )
    path('<int:grade>/<str:sub>/<str:prof>/', include(router.urls),name='mainboard'),
    path('', grade_list ,name = 'get_grade'),
    path('<int:grade>/', sub_list, name ='get_sub'),
    path('<int:grade>/<str:sub>/', prof_list, name = 'get_prof'),
    # path('posts/',post_list),
    # path('posts/<int:pk>/', post_deatil),
]