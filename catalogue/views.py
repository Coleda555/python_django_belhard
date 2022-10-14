from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render

from .models import Category, SubCategory, Product

from .forms import Calculator, FeedbackForm

mixin = {
    'facebook': {'https://vk.com/bogdanovich_a'},
    'instagram': {'https://instagram.com/pilot_kaliada'}
}


def catalogue(request: HttpRequest):
    cat = Category.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'catalogue/index.html', {
        'categories': cat,
        'products': products,
        'feedback_form': FeedbackForm()
    })


# # def index(request: HttpRequest):
# #     categories = Category.objects.all().order_by('-name')
# #     products = Product.objects.all()
# #
# #     return render(request, 'catalogue/index.html', {
# #         'categories': categories,
# #         'menu': ['Menu 1', 'Menu 2'],
# #         'products': products,
#
#     })


def index2(request):
    cat = Category.objects.all()
    products = Product.objects.all()
    result = None
    if request.method == 'POST':
        result = int(request.POST.get('width')) * int(request.POST.get('height'))
    return render(request, 'catalogue/index2.html', {
        'categories': cat,
        'products': products,
        'calculator_form': Calculator(),
        'result': result,
        'feedback_form': FeedbackForm()
    })



def catalogue_from_id(request: HttpRequest, from_id: int):
    categories = Category.objects.filter(id__gte=from_id)
    subcategories = SubCategory.objects.all()
    data = {}
    for category in categories:
        data[category.name] = []
        for subcategory in subcategories:
            if subcategory.category.id == category.id:
                data[category.name].append(subcategory.name)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def catalogue_from_to_id(request: HttpRequest, from_id: int, to_id: int):
    categories = Category.objects.filter(
        id__gte=from_id,
        id__lte=to_id
    )
    subcategories = SubCategory.objects.all()
    data = {}
    for category in categories:
        data[category.name] = []
        for subcategory in subcategories:
            if subcategory.category.id == category.id:
                data[category.name].append(subcategory.name)
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


def error404(request, exceptioon):
    return HttpResponse('<b><i>404 NOT FOUND</b></i>')
