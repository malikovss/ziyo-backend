from modeltranslation.translator import register, TranslationOptions

from .models import Article, Category


@register(Article)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')


@register(Category)
class CategoryTranslations(TranslationOptions):
    fields = ('title',)
