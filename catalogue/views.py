from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

from .models import Category, SubCategory


def catalogue(request: HttpRequest):
    categories = Category.objectss.all().order_by('id')
    subcategories = SubCategory.oblects.all()
    data = {}
    for category in categories:
        data[category.name] = []
        for subcategory in subcategories:
            if subcategory.category.id == category.id:
                data[category.name].append((subcategory.name))
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def catalogue_from_to_id(request: HttpRequest, from_id: int, to_id: int):
