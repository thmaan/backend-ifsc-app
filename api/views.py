from django.shortcuts import render, redirect 

from rest_framework.parsers import JSONParser
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.decorators import parser_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import *

from .serializers import  CategorySerializer

@api_view(['GET'])
def hello(request):
	context= 'ola amigo'

	return Response(context,status=201)

@api_view(['GET'])
def getCategoryApi(request):
	categories = Category.objects.all()
	serializer = CategorySerializer(categories, many=True)
	
	return Response(serializer.data, status=201)