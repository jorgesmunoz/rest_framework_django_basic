from profiles_api import views
from django.urls import path

app_name = 'profiles_api'

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
