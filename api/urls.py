from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [    
    path('create-category-api/', views.createCategoryApi, name ='create-category-api'),
    
    path('hello/', views.hello, name='hello'),
]