from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import resolve
from rest_framework import status
from rest_framework.views import APIView, Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .serializer import SnippetSerializer
# from .models import UserManager
# Create your views here.
from . import urls
class Index(APIView):
    def get(self, request):
        def replace_all(charlist, _str, _replace):
            for i in charlist:
                _str = _str.replace(i, _replace)
            return _str
        # return all endpoints 
        print(request.get_full_path())
        endpoints = {}
        for i in urls.urlpatterns:
            endpoint    = i.pattern.__str__()
            key         = replace_all(['-', '/'], endpoint, '_')
            url = 'https://' if request.is_secure() else 'http://' + request.get_host() + '/' + endpoint 

            if endpoint == '':
                continue

            endpoints[key] = url
        return JsonResponse(endpoints, safe=False)

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

class ObtainExpiringAuthToken(APIView):
    def post(self, request):
        if 'username' in request.POST and 'password' in request.POST:
            username    = request.POST['username']
            password    = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)

                if not created:
                    token.created = datetime.utcnow()
                    token.save()
                return Response({'token': token.key})
            return HttpResponse('error')


# Working with serializers
class SnippetDetail(APIView):
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)