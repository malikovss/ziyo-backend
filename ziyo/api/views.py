from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from . import models, serializers, permissions


class ArticleView(ModelViewSet):
    # permission_classes = [permissions.IsAdminOrReadOnly,]
    queryset = models.Article.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'category__title', 'status', 'type', 'top']

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.ArticleDetailSerializer
        return serializers.ArticleSerializer


class PhotoView(ModelViewSet):
    # permission_classes = [permissions.IsAdminOrReadOnly,]
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer


class CategoryView(ModelViewSet):
    # permission_classes = [permissions.IsAdminOrReadOnly,]
    queryset = models.Category.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.CategoryDetailSerializer
        return serializers.CategorySerializer


class TvView(ModelViewSet):
    # permission_classes = [permissions.IsAdminOrReadOnly,]
    queryset = models.Tv.objects.all()
    serializer_class = serializers.TvSerializer


class TvProgramView(ModelViewSet):
    # permission_classes = [permissions.IsAdminOrReadOnly,]
    queryset = models.TvProgram.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return serializers.TvProgramDetailSerializer
        return serializers.TvProgramSerializer
