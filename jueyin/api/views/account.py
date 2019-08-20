import uuid

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models

class AuthView(APIView):
    # def options(self, request, *args, **kwargs):
    #     """
    #     预检
    #     :param request:
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     """
    #     obj = HttpResponse('')
    #     obj['Access-Control-Allow-Origin'] = "*"
    #     obj['Access-Control-Allow-Headers'] = "Content-Type"
    #     return obj


    def post(self, request, *args, **kwargs):
        print(request.data)

        # obj = Response('...')
        # obj['Access-Control-Allow-Origin'] = "*"
        # return obj

        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user = models.UserInfo.objects.filter(user=user, pwd=pwd).first()

        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误啦'
        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user, defaults={'token': uid})
            ret['token'] = uid
        return Response(ret)
