from django.urls import path
from . import views
urlpatterns = [
    path('', views.ExampleView.as_view()),
    path('get-token', views.ObtainExpiringAuthToken.as_view())
]