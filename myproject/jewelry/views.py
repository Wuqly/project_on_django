from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddJewelryForm, UploadFileForm
from .models import Jewelry, Types, UploadFiles

import logging

from .utils import DataMixin

logger = logging.getLogger(__name__)

# Create your views here.



class JewelryHome(DataMixin, ListView):
    template_name = 'jewelry/main.html'
    context_object_name = 'cards'
    title_page = 'Главная страница'

    def get_queryset(self):
        return Jewelry.published.all().order_by('type')



class ShowCard(DataMixin,DetailView):
    template_name = 'jewelry/card.html'
    slug_url_kwarg = 'card_slug'
    context_object_name = 'card'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title = context['card'].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Jewelry.published, slug=self.kwargs[self.slug_url_kwarg])

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
    return render(request, 'jewelry/about.html', {'title': 'О нас', 'form': form})


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')



class JewelryCatalog(DataMixin,ListView):
    template_name = 'jewelry/index.html'
    context_object_name = 'cards'
    allow_empty = False

    def get_queryset(self):
        return Jewelry.published.filter(type__slug=self.kwargs['cat_slug']).select_related('type')
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        type = context['cards'][0].type
        return self.get_mixin_context(context, title = 'Тип - '+ type.name)

def contact(request):
    return HttpResponse('Обратная связь')

def login(request):
    return render(request, 'jewelry/sign.html', { 'title': 'Авторизация'})
    

class AddProduct(DataMixin,CreateView):
    form_class = AddJewelryForm
    template_name = 'jewelry/add_product.html'
    title_page = 'Добавление товара'


class UpdateProduct(DataMixin, UpdateView):
    model = Jewelry
    fields = '__all__'
    template_name = 'jewelry/add_product.html'
    success_url =  reverse_lazy('home')
    title_page = 'Редактирование товара'


"""class AddProduct(View):
    def get(self, request):
        form = AddJewelryForm()
        data = {
        'title': 'Добавление товара',
        'menu': menu,
        'form': form,
        }
        return render(request, 'jewelry/add_product.html', data)

    def post(self, request):
        form = AddJewelryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
        'title': 'Добавление товара',
        'menu': menu,
        'form': form,
        }
        return render(request, 'jewelry/add_product.html', data)"""


'''def index(request):
    cards = Jewelry.publiched.all().order_by('type')
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'cards': cards,
        'cats': catalog_db,
    }

    return render(request, 'jewelry/main.html', data)'''


"""def show_card(request, card_slug):
    card = get_object_or_404(Jewelry, slug=card_slug)
    data = {
        'title': card.title,
        'menu': menu,
        'card': card,
        'cats': catalog_db,
    }

    return render(request, 'jewelry/card.html', data)"""

"""def catalog(request, cat_slug):
    catalog = get_object_or_404(Types, slug=cat_slug)
    cards = Jewelry.publiched.filter(type_id = catalog.pk).select_related('type')
    data = {
        'title': catalog.name,
        'menu': menu,
        'cards': cards,
        'catalog': catalog.pk,
    }

    return render(request, 'jewelry/index.html', context=data)"""


'''def add_product(request):
    if request.method == 'POST':
        form = AddJewelryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                Jewelry.objects.create(**form.cleaned_data)
                return redirect('home')
            except Exception as e:
                logger.error(f"Ошибка добавления товара: {e}")
                form.add_error(None, 'Ошибка добавления товара')
            
            form.save()
            return redirect('home')
    else:
        form = AddJewelryForm()
        
    data = {
        'title': 'Добавление товара',
        'menu': menu,
        'form': form,
    }
    return render(request, 'jewelry/add_product.html', data)'''




