from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated  
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.decorators import parser_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from .models import *

from .serializers import  CategorySerializer, NewsSerializer, TagsSerializer

from .models import News
from .forms import NewsForm
from taggit.models import Tag
from django.forms.models import model_to_dict

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def home(request):
    news = News.objects.order_by('-published')[:10]
    common_tags = News.tags.most_common()[:4]
    form = NewsForm(request.POST)
    if form.is_valid():
        new_news = form.save(commit=False)
        new_news.slug = slugify(new_news.title)
        new_news.save()
        form.save_m2m()
        return redirect('/')
    context = {
        'news':news,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'api/home.html', context)
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    context = {
        'news':news,
    }
    return render(request, 'api/detail.html', context)
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter news by tag name  
    news = News.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'news':news,
    }
    return render(request, 'api/tag.html', context)
    
@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def hello(request):
	context= 'ola amigo'

	return Response(context,status=201)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getCategoryApi(request):
	categories = Category.objects.all()
	serializer = CategorySerializer(categories, many=True)
	
	return Response(serializer.data, status=201)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getTagsApi(request):
    news = News.objects.order_by('-published').distinct()
    serializer = TagsSerializer(news, many=True)

    return Response(serializer.data, status=201)

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getNewsApi(request):
    news = News.objects.all()

    serializer = NewsSerializer(news, many=True)
    
    return Response(serializer.data, status=201)

@api_view(['POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def getSpecificNewsApi(request):
    data = request.data['tags']
    tag = get_object_or_404(Tag, slug=data)
    news = News.objects.filter(tags=tag)
    serializer = NewsSerializer(news, many=True)

    return Response(serializer.data, status=201)