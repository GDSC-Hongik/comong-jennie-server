from rest_framework import serializers
from .models import Post

# class PostlistSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title']
        
class PostdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
      
class GradePostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','id','sub','profs']
        
class SubPostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','id','profs']
        
class ProfsPostlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','id',]
        
# class BoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Board
#         fields = ['grade']
# class Subserializer(serializers.ModelSerializer):
#     class Meta :
#         model = Board
#         fields = ['sub']
# class Profserializer(serializers.ModelSerializer):
#     class Meta :
#         model = Board
#         fields = ['profs']