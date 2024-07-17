from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sign_up_view,name="signup_url"),
    path('check_user/', views.check_user,name="check_user_url"),
    path('signin/', views.sign_in,name="signin_url"),
    
]
