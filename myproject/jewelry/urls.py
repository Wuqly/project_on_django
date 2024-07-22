from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')  

urlpatterns = [
    path('', views.JewelryHome.as_view(), name = 'home'),
    path('about/', views.about, name = 'about'),
    path('catalog/<slug:cat_slug>/', views.JewelryCatalog.as_view(), name = 'catalog'),
    path('contact/', views.contact, name = 'contact'),
    path('login/', views.login, name = 'login'),
    path('add_product/', views.AddProduct.as_view(), name = 'add_product'),
    path('card/<slug:card_slug>/', views.ShowCard.as_view(), name='card'),
    path('edit_product/<slug:slug>/', views.UpdateProduct.as_view(), name='edit_product'),

]
