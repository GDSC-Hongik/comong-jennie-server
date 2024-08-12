from rest_framework import serializers
from .models import Notice ,Sub_post,Join_post

# 전공 게시판
class GradePostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_post
        fields = ['title','id','content','sub','profs','dt_created']
        
class SubPostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_post
        fields = ['title','id','content','profs','dt_created']
        
class ProfsPostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_post
        fields = ['title','id','content','dt_created']
        
class PostdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_post
        fields = '__all__'
     
# 공지사항       
class NoticelistSerializer(serializers.ModelSerializer):
    class Meta :
        model = Notice
        fields = '__all__'

# 구인게시판
class JoinpostlistSerializer(serializers.ModelSerializer):
    class Meta :
        model = Join_post
        fields = ['title','id','dt_created','participants_num','current_num']


class JoinpostdetailSerializer(serializers.ModelSerializer):
    class Meta :
        model = Join_post
        fields = '__all__'
        
