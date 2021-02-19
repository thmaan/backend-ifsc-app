from rest_framework import serializers
from .models import Category, News
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from django.contrib.auth import get_user_model

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

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username','password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user