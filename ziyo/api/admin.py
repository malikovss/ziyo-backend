from django.contrib import admin
from . import models


admin.site.register(models.Photo)
admin.site.register(models.Article)
admin.site.register(models.Tv)
admin.site.register(models.TvProgram)
admin.site.register(models.Category)