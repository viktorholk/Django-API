from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view()),
    path('get-token', views.ObtainExpiringAuthToken.as_view(), name='Get the token')
]