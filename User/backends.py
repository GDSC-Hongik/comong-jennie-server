import jwt

from django.conf import settings
from rest_framework import authentication,exceptions

from .models import User

class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    # authenticate 메소드 : endpoint에 인증 필요한지 여부와 상관없이 모든 request에서 호출됨
    def authenticate(self, request):
        
        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        # auth_header는 2가지 요소를 배열로 갖고 있어야 함
        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None
        
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')
        
        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request,token)
        # 1) None : 어떤 요청의 header에 token 포함하지 않은 경우 -> 인증 실패한 경우
        # 2) (user,token) : 인증이 성공적으로 이루어졌을 경우
        # 3) 반환 x : error 발생, AuthenticationFailed error 보내고, 나머지는 drf가 처리

    # 위 과정 통과한 user에게 접근 허용
    # 인증 성공 -> user,token 반환 / 실패 -> error 반환
    def _authenticate_credentials(self,request,token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except:
            msg = 'Invalid authentication. Could not decode token.'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'No user matching this token was found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = 'This user has been deactivated.'
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)