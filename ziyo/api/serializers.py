from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from . import models


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'
        read_only_fields=["thumb"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CategoryDetailSerializer(ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    class Meta:
        model = models.Category
        fields = '__all__'
        include = ['photo',]
        


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'

class ArticleDetailSerializer(ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = models.Article
        fields = '__all__'
        include = ['photo', 'category',]


class TvProgramSerializer(ModelSerializer):
    class Meta:
        model = models.TvProgram
        fields = '__all__'

class TvProgramDetailSerializer(ModelSerializer):
    photo = PhotoSerializer(read_only=True)
    class Meta:
        model = models.TvProgram
        fields = '__all__'
        include='photo'


class TvSerializer(ModelSerializer):
    class Meta:
        model = models.Tv
        fields = '__all__'