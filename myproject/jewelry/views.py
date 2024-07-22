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







