from rest_framework.views import exception_handler


def core_exception_handler(exc, context):

    # drf에서 제공하는 exception_handler
    response = exception_handler(exc, context)
    
    # 직접 처리할 수 있는 exception error 보관
    handlers = {
        'ValidationError': _handle_generic_error
    }
    
    # exception type 식별 (drf handler로 처리 / 직접 처리)
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response) # 직접 처리할 수 있는 exception error이면 -> 직접 처리
    return response # 아니면 -> drf handler로 처리

def _handle_generic_error(exc, context, response):
    response.data = {
        'errors': response.data # response.data에는 error key, error 메시지 담겨 있음
    }

    return response