from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponsePermanentRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404 
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from django.core.paginator import Paginator

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


class Catalog(DataMixin, ListView):
    template_name = 'jewelry/catalog.html'
    context_object_name = 'cards'
    title_page = 'Каталог'

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
    contact_list = Jewelry.objects.all()
    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'jewelry/about.html', {'title': 'О нас', 'page_obj': page_obj})


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


    
class AddProduct(LoginRequiredMixin,UserPassesTestMixin,DataMixin,CreateView):
    form_class = AddJewelryForm
    template_name = 'jewelry/add_product.html'
    title_page = 'Добавление товара'
    login_url = 'users:login'  # URL для перенаправления неавторизованных пользователей
    redirect_field_name = 'next' 

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect(self.request.get_full_path(), self.login_url, self.redirect_field_name)
        return render(self.request, 'jewelry/permission_denied.html')

class UpdateProduct(DataMixin, UpdateView):
    model = Jewelry
    fields = '__all__'
    template_name = 'jewelry/add_product.html'
    success_url =  reverse_lazy('home')
    title_page = 'Редактирование товара'





