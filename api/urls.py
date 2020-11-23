from django.urls import path
from . import views
urlpatterns = [
    path('', views.ExampleView.as_view()),
    path('login', views.Login.as_view()),
    path('register', views.Register.as_view())
]