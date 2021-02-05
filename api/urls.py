from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [    
    path('', views.home, name="home"),
    path('detail/<str:slug>', views.detail, name="detail"),
    path('tag/<str:slug>', views.tagged, name="tagged"),

    path('get-category-api/', views.getCategoryApi, name ='get-category-api'),
    path('get-news-api/', views.getNewsApi, name ='get-news-api'),
 	path('get-specific-news-api/', views.getSpecificNewsApi, name ='get-specific-news-api'),
    path('hello/', views.hello, name='hello'),
]