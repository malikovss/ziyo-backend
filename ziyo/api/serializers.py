from rest_framework import serializers

from . import models


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'
        read_only_fields = ["thumb"]


class CategorySerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = models.Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ArticleDetailSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = models.Article
        fields = '__all__'


class TvProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TvProgram
        fields = '__all__'


class TvProgramDetailSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(read_only=True)

    class Meta:
        model = models.TvProgram
        fields = '__all__'


class TvSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tv
        fields = '__all__'
