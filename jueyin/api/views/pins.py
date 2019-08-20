from rest_framework.views import APIView
from rest_framework.response import Response
from api.util import auth

class PinsView(APIView):
    authentication_classes = [auth.PinsAuth]
    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.auth)

        return Response('超级会员专属')
