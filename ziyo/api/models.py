import os
from django.db import models
from PIL import Image
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from string import ascii_letters
from random import choices

TYPE_CHOICES = [
    ('1', 'news'),
    ('2', 'photo-news'),
    ('3', 'video-news'),
    ('4', 'slider'),
]

STATUS_CHOICE = [
    ('0', '0'),
    ('1', '1'),
]


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar')


class Photo(models.Model):
    image = models.ImageField()
    thumb = models.JSONField(null=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        name, ext = os.path.splitext(self.image.name)
        name = slugify(name) + "_" + "".join(choices(ascii_letters, k=7))
        size = self.image.size
        path = f"{settings.MEDIA_ROOT}thumb/{name}_"
        if ext in settings.EXT:
            thumbnails = {}
            thumb = settings.THUMB
            with Image.open(self.image) as image:
                for t in thumb:
                    img = image.copy()
                    size = (thumb[t]['w'], thumb[t]['h'])
                    img.thumbnail(size)
                    p = path + thumb[t]['slug'] + ext
                    img.save(p)
                    thumbnails[t] = {
                        "w": thumb[t]['w'],
                        "h": thumb[t]['h'],
                        "slug": thumb[t]['slug'],
                        "path": p,
                        "link": settings.HOSTNAME + p,
                    }
            self.thumb = thumbnails
        super(Photo, self).save()

    def delete(self):
        try:
            os.remove(self.image.path)
            for t in self.thumb:
                path = self.thumb[t]["path"]
                os.remove(path)
        except:
            pass
        super(Photo, self).delete()

    def __str__(self) -> str:
        return self.image.name


class TvProgram(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)
    link = models.CharField(max_length=250)
    photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to="tv_program_file", null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title

    def delete(self):
        try:
            os.remove(self.photo.path)
            os.remove(self.file.path)
        except:
            pass
        super().delete()


class Tv(models.Model):
    title = models.CharField(max_length=150)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default=1)
    slug = models.TextField()
    link_hi = models.TextField()
    link_low = models.TextField()
    link_mid = models.TextField()
    photo = models.ImageField()

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title

    def delete(self):
        try:
            os.remove(self.photo.path)
        except:
            pass
        super().delete()


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    photo = models.ForeignKey('Photo', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="1", null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    content = models.TextField(null=True, blank=True)
    photo = models.ManyToManyField('Photo', blank=True)
    category = models.ManyToManyField('Category', blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='1')
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='1')
    top = models.CharField(max_length=1, choices=STATUS_CHOICE, default='0')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
