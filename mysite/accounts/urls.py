from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
	path('', views.loginPage, name="home"),
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]