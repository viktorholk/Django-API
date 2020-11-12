from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
# Create your views here.
def basepoint(request):
    return JsonResponse({"hello": "world"})

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

