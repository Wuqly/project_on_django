from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse
from django.template.loader import render_to_string

from .forms import AddJewelryForm, UploadFileForm
from .models import Jewelry, Types, UploadFiles

import logging

logger = logging.getLogger(__name__)

# Create your views here.
catalog_db = Types.objects.all()

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Каталог', 'url_name': 'catalog'},
        {'title': 'Добавить товар', 'url_name': 'add_product'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

def index(request):
    cards = Jewelry.objects.all().order_by('type')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'cards': cards,
        'cats': catalog_db,
    }

    return render(request, 'jewelry/main.html', data)

def show_card(request, card_slug):
    card = get_object_or_404(Jewelry, slug=card_slug)
    data = {
        'title': card.title,
        'menu': menu,
        'card': card,
        'cats': catalog_db,
    }

    return render(request, 'jewelry/card.html', data)
    

def handle_uploaded_file(f):
    with open(f"image/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'jewelry/about.html', {'title': 'О нас', 'menu': menu, 'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def catalog(request, cat_slug):
    catalog = get_object_or_404(Types, slug=cat_slug)
    cards = Jewelry.publiched.filter(type_id = catalog.pk)
    data = {
        'title': catalog.name,
        'menu': menu,
        'cards': cards,
        'catalog': catalog.pk,
    }

    return render(request, 'jewelry/index.html', data)

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return render(request, 'jewelry/sign.html', {'menu': menu, 'title': 'Авторизация'})


def add_product(request):
    if request.method == 'POST':
        form = AddJewelryForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('home')
    else:
        form = AddJewelryForm()
        
    data = {
        'title': 'Добавление товара',
        'menu': menu,
        'form': form,
    }
    return render(request, 'jewelry/add_product.html', data)

