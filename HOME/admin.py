from django.contrib import admin
from .models import Portfolio_Site, Tech


@admin.register(Portfolio_Site)
class Portfolio_SiteAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Tech)
class TechAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
