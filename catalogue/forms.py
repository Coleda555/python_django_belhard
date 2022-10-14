from django.forms import Form, IntegerField, TextInput, CharField, ModelForm, Textarea
from .models import Feedback


class Calculator(Form):
    width = IntegerField(min_value=1, widget=TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Введите ширину посылки',
            'min': '1'
        }
    ))
    height = IntegerField(min_value=1, widget=TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number',
            'placeholder': 'Введите высоту посылки',
            'min': '1'
        }
    ))
    color = CharField(widget=TextInput(
        attrs={
            'class': 'form-control',
            'type': 'color',
            'placeholder': 'выберите цвет'
        }
    ))


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'phone_number', 'message')
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'name',
                    'type': 'text',
                    'placeholder': 'Enter your name...',
                    'data-sb-validations': 'required'
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'type': 'email',
                    'placeholder': 'kaliada-biz@yandex.ru',
                    'data-sb-validations': 'required,email'
                }
            ),
            'phone_number': TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'phone',
                    'type': 'tel',
                    'placeholder': '+375332020327',
                    'data-sb-validations': 'required'
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'id': 'message',
                    'type': 'text',
                    'placeholder': 'Enter your feedback here...',
                    'data-sb-validations': 'required'
                }
            ),
        }