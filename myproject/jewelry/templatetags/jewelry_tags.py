from django import template
import jewelry.views as views
from jewelry.models import Types
from jewelry.utils import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu

@register.inclusion_tag('jewelry/catalogs.html')
def show_catalog():
    cats = Types.objects.all()
    return {'cats': cats}