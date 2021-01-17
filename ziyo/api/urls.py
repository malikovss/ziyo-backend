from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


router = DefaultRouter()
router.register('photo', views.PhotoView)
router.register('category', views.CategoryView)
router.register('article', views.ArticleView)
router.register('tv-program', views.TvProgramView)
router.register('tv', views.TvView)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
