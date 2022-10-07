from django.urls import path

from catalogue.admin import belhard_admin_site

from .views import catalogue

urlpatterns = [
    path('', catalogue),
    path('from/<int:from_id>', catalogue),
]
