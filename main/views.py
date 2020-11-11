from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def basepoint(request):
    return JsonResponse({"hello": "world"});