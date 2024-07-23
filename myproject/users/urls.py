from django.urls import path, register_converter
from . import views 

urlpatterns = [
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),

]
