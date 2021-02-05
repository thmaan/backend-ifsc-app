from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [    
    path('get-category-api/', views.getCategoryApi, name ='get-category-api'),
    
    path('hello/', views.hello, name='hello'),
]