from rentalspace import serialize
from rentalspace import serialize
from rentalspace.models import VansModel
from rentalspace.serialize import VansSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serialize import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class VansModel(viewsets.ModelViewSet):
    queryset = VansModel.objects.all()
    serializer_class = VansSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


    # def get(self, request):
    #     vansObj=VansModel.objects.all()
    #     vnSeralizeObj = VansSerializer(vansObj, many = True)
    #     return Response(vnSeralizeObj.data)

    # def post(self, request):
    #     serializeObj = VansSerializer(data = request.data)
    #     if serializeObj.is_valid():
    #         serializeObj.save()
    #         return Response(200)
    #     return Response(serializeObj.errors)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})