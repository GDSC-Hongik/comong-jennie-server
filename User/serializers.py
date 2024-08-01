from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from django.utils import timezone

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
'''
# 회원가입
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True # password는 update,create할 때는 사용 / serialize할때는 포함X
    )

    token = serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model = User
        fields = [
            'email', 
            'username',
            'nickname',
            'password',
            'token'
        ]
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)

# 로그인  
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255,read_only=True) # 반환값으로만 사용, 입력받지 X
    password = serializers.CharField(max_length=128,write_only=True) # 입력만 받음, 반환값으로 출력 X
    last_login = serializers.CharField(max_length=255,read_only=True) # 반환값으로만 사용, 입력받지 X

    # validate 메소드 : 현재 LoginSerializer의 instance가 유효한지 확인
    # user가 로그인 시도 -> validate ->  로그인 성공 여부 반환 
    def validate(self,data):
        email = data.get('email',None)
        password = data.get('password',None)

        # email, password 중 하나라도 입력되지 않은 경우 오류 메시지 출력
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        # authenticate 메소드 : 입력받은 email, password 조합 -> db의 email, password 조합과 매칭 -> 매칭되는 조합이 없을 경우 None 반환
        user = authenticate(username=email, password=password)

        # user 없을 경우, 비활성화됐을 경우 오류 메시지 출력
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        
        # user의 마지막 로그인 시간 업데이트
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])

        # 모든 유효성 검사 끝난 후 반환
        return{
            'email':user.email,
            'username':user.username,
            'last_login':user.last_login
        }
    
# 프로필 수정
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length = 128,
        min_length = 8,
        write_only = True # password는 update,create할 때는 사용 / serialize할때는 포함X
    )
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'token'
        ]

        read_only_fields = ('token',)
    
    def update(self,instance,validated_data):
        password = validated_data.pop('password',None) # password는 setattr로 처리하지 않기 위해 validated_data dict에서 제거

        # validated_data(업데이트 된 데이터)를 key,value값으로 setattr메소드에 전달
        for (key,value) in validated_data.items():
            # setattr 메소드 : 현재 user 속성값 바꿔줌
            setattr(instance,key,value) # instance = 요청한 user정보(객체)
        
        # password는 따로 처리
        if password is not None:
            instance.set_password(password)
        
        # 변경된 instance 정보 저장(db에는 저장X, view의 serializer.save()가 db에 저장)
        instance.save()

        return instance

