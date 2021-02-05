from rest_framework import serializers
from .models import Category, News
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(TaggitSerializer, serializers.ModelSerializer):

	tags = TagListSerializerField()
	
	class Meta:
		model = News
		fields = '__all__'

class TagsSerializer(TaggitSerializer):
	
	tags = TagListSerializerField()
