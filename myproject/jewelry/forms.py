from django import forms
from .models import Jewelry, Types
from django.core.exceptions import ValidationError

class AddJewelryForm(forms.ModelForm):
    '''image = forms.ImageField(required=False,label='Фото')
    title = forms.CharField(max_length=200, label='Название')
    slug = forms.SlugField(max_length=200, label='URL')
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label='Тип товара', empty_label='Тип не выбран')
    quantity = forms.IntegerField(label='Количество')
    price = forms.CharField(max_length=200, label='Цена')
    is_published = forms.BooleanField(label='Статус', initial=True)''' 

    type = forms.ModelChoiceField(queryset=Types.objects.all(), label='Тип товара', empty_label='Тип не выбран')
    class Meta:
        model = Jewelry
        fields = ['image','title','slug','type','quantity','price','is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
        }

        labels = {'slug': 'URL'}


    def clean_title(self):
        title = self.cleaned_data['title']
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError('Должны присутствовать только русские символы, дефисы и порбелы')
        return title
    
    
    def clean_price(self):
        price = self.cleaned_data['price']
        ALLOWED_CHARS_PRICE = '1234567890 '
       
        if not (set(price) <= set(ALLOWED_CHARS_PRICE)):
            raise forms.ValidationError('Должны присутствовать только цифры и пробелы')
        return price
    

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл') 