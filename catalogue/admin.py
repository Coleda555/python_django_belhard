from django.contrib import admin

from .models import Category, SubCategory


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с побликации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)
    search_help_text = 'Имя категории'
    actions = (make_published, make_unpublished)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('name',)
    search_help_text = 'Имя категории'
    actions = (make_published, make_unpublished)


class BelhardAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'SITE TITLE'
    site_url = '/admin'
    index_title = 'INDEX TITLE'


belhard_admin_site = BelhardAdminSite()

belhard_admin_site.register(Category, CategoryAdmin)
belhard_admin_site.register(SubCategory, SubCategoryAdmin)
