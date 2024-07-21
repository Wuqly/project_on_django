from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')  

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('catalog/<slug:cat_slug>/', views.catalog, name = 'catalog'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.login, name = 'login'),
    path('add_product/', views.add_product, name = 'add_product'),
    path('card/<slug:card_slug>/', views.show_card, name='card'),
]
