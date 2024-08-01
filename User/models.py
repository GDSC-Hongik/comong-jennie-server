'''
from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .validators import validate_no_special_characters

import jwt
from datetime import datetime,timedelta

from django.conf import settings

class TimestampedModel(models.Model):
    # 생성된 날짜를 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정된 날짜를 기록
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class User(AbstractUser,PermissionsMixin,TimestampedModel):
    nickname = models.CharField(
        max_length=15,
        unique=True, 
        null= True,
        validators=[validate_no_special_characters],
        error_messages= {"unique": "이미 사용중인 닉네임입니다."},                      
    )

    profile_pic = models.ImageField(
        default = "default_profile_pic.jpg", upload_to="profile_pics"
    ) 
    
    def __str__(self):
        return self.email
    
    @property
    def token(self):
        return self._generate_jwt_token( )

    def _generate_jwt_token(self):
        dt = datetime.now( ) + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.timestamp()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
'''
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField

from .managers import UserManager

import jwt
from datetime import datetime, timedelta
from django.conf import settings

class TimestampedModel(models.Model):
	
    # 생성된 날짜를 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정된 날짜를 기록
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    phonenumber = models.CharField(max_length=255)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
        'username',
        'phone_number'
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.nickname
    
    def get_full_name(self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    @property
    def token(self):
        return self._generate_jwt_token( )

    def _generate_jwt_token(self):
        dt = datetime.now( ) + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.timestamp()
        }, settings.SECRET_KEY, algorithm='HS256')

        return token