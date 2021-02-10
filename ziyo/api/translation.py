from modeltranslation.translator import register, TranslationOptions

from .models import Article


@register(Article)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')
