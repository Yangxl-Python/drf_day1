from django.urls import path

from api import views

urlpatterns = [
    path('emp/', views.EmployeeAPIView.as_view()),
    path('emp/<pk>/', views.EmployeeAPIView.as_view()),

    path('stu/', views.StudentAPIView.as_view()),
    path('stu/<pk>/', views.StudentAPIView.as_view()),
]
