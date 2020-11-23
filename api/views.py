from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
# from .models import UserManager
# Create your views here.
class ExampleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponse("'you're in")

class Login(APIView):
    def post(self, request):
        if 'username' in request.POST and 'password' in request.POST:
            username    = request.POST['username']
            password    = request.POST['password']
            return HttpResponse(authenticate(username=username, password=password))
        return HttpResponse('Username and password field must be provided')

class GetToken(APIView):
    def post(self, request):
        if 'username' in request.POST and 'password' in request.POST:
            username    = request.POST['username']
            password    = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                token = Token.objects.get_or_create(user=user)
                print(token[0])
                return HttpResponse()
            return HttpResponse('error')


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                # update the created time of the token to keep it valid
                token.created = datetime.datetime.utcnow()
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()