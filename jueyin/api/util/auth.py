from rest_framework.authentication import BaseAuthentication
from api import models
from rest_framework.exceptions import AuthenticationFailed

class PinsAuth(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get('token')
        obj = models.UserToken.objects.filter(token=token).first()
        if not obj:
            raise AuthenticationFailed({'code': 1001, 'error': '认证失败'})
        return (obj.user.user, obj)