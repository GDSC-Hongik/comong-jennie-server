import json
from rest_framework.renderers import JSONRenderer

class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self,data,media_type=None,renderer_context=None):
        
        # 만약 view가 error 던지면 -> 내부 data는 errors에 담김
        errors = data.get('errors',None)

        # data 안에 있는 token 받음(byte 형태)
        token = data.get('token',None)

        # data에 errors가 있는지 확인
        if errors is not None:
            return super(UserJSONRenderer,self).render(data) # errors가 있다면 data를 user key에 넣지 않고 그대로 반환

        # decode : byte 형태는 직렬화 못하기 때문에, rendering 전에 decode 해야함
        if token is not None and isinstance(token,bytes):
            data['token'] = token.decode('utf-8')
        
        # render : data를 user 안에 담아 json 형태로 render함.
        return json.dumps({
            'user':data
        })