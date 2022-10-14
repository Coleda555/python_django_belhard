from django.urls import path, register_converter

from .views import catalogue_from_id, catalogue_from_to_id, index2,  catalogue


class MyConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(MyConverter, 'yyyy')

urlpatterns = [
    path('', catalogue),
    path('index/', index2, name='index'),
    path('<int:from_id>', catalogue_from_id),
    path('<int:from_id>/<int:to_id>', catalogue_from_to_id),

]
