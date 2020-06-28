from django.urls import path

from app1 import views

urlpatterns = [
    path('user/', views.users),
    path('users/', views.UserView.as_view()),
    path('users/<pk>/', views.UserView.as_view()),

    path('api_user/', views.UserAPIView.as_view()),
    path('api_user/<pk>/', views.UserAPIView.as_view()),
]