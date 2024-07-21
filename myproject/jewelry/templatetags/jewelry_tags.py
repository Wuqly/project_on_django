from django import template
import jewelry.views as views
from jewelry.models import Types

register = template.Library()


@register.inclusion_tag('jewelry/catalogs.html')
def show_catalog():
    cats = Types.objects.all()
    return {'cats': cats}