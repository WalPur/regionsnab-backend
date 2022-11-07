from django.contrib import admin
from .models import News, NewsImage

# Register your models here.
class ImagesInline(admin.TabularInline):
    model = NewsImage
    extra = 0


@admin.register(News)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_desc']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [ImagesInline, ]
