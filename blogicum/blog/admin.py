from django.contrib import admin
from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'description',
        'slug',
        'created_at'
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'title',
        'slug',
        'created_at'
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at'
    )
    list_display_links = (
        'name',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'name',
        'created_at'
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'text',
        'pub_date',
        'author',
        'category',
        'location',
        'created_at'
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'is_published',
    )
    list_filter = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'created_at'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
