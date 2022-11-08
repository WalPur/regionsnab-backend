from django.contrib import admin
from .models import News, NewsImage, partnerShip

# Register your models here.
class ImagesInline(admin.TabularInline):
    model = NewsImage
    extra = 0


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_desc']
    list_filter = ['title']
    search_fields = ['title']
    inlines = [ImagesInline, ]


@admin.register(partnerShip)
class PartnerShip(admin.ModelAdmin):
    list_display = ['surname', 'first_name', 'patronymic', 'email', 'phone']
    list_filter = ['surname', 'first_name', 'patronymic']
    search_fields = ['surname', 'first_name', 'patronymic']
