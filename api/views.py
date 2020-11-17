from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
            print((username, password))
            return HttpResponse(authenticate(username=username, password=password))
        return HttpResponse('No user infomation was provided')
