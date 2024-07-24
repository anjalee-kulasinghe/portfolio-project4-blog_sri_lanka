from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'featured', 'display_image')
    
    def display_image(self, obj):
        if obj.articale_image:
            return mark_safe(f'<img src="{obj.articale_image.url}" width="100" height="100"/>')
        return 'No image'
    display_image.short_description = 'Image'

admin.site.register(Article, ArticleAdmin)
