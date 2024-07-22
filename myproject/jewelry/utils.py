from .models import Types

catalog = Types.objects.all()

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Каталог', 'url_name': 'catalog'},
        {'title': 'Добавить товар', 'url_name': 'add_product'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]

class DataMixin:
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if 'menu' not in self.extra_context:
            self.extra_context['menu'] = menu

        if 'catalog' not in self.extra_context:
            self.extra_context['catalog'] = catalog
    
    def get_mixin_context(self, context, **kwargs):
        context['menu'] = menu
        context['catalog'] = catalog
        context.update(kwargs)
        return context
    
