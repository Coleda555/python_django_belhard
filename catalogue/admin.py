from django.contrib import admin

from .models import Category, SubCategory, Product, Feedback


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
    fieldsets = (('Основное',
                  {
                      'fields': ('name', 'category'),
                      'description': 'Основные параметры'
                  }),
                 ('Дополнительное',
                  {
                      'fields': ('is_published', 'descr', 'count', 'image')
                  }))
    list_editable = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)
    search_help_text = 'Имя продукта'
    actions = (make_published, make_unpublished)

class BelhardAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'SITE TITLE'
    site_url = '/admin'
    index_title = 'INDEX TITLE'
    #index_template = путь к шаблону HTML


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date_created')
    list_filter = ('email', 'phone_number')
    date_hierarchy = 'date_created'



class FeedbackManager(FeedbackAdmin):
    readonly_fields = ('date_created', 'email', 'phone_number', 'message', 'name')


belhard_admin_site = BelhardAdminSite(name='belhard_admin_site')

belhard_admin_site.register(Category, CategoryAdmin)
belhard_admin_site.register(SubCategory, SubCategoryAdmin)
belhard_admin_site.register(Product, ProductAdmin)
belhard_admin_site.register(Feedback, FeedbackManager)

