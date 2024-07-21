from django.contrib import admin, messages
from .models import Jewelry, Types, UploadFiles
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(Jewelry)
class JewelryAdmin(admin.ModelAdmin):
    fields = ['image','photo','title','slug','type','quantity', 'price', 'is_published']
    readonly_fields = ['photo']
    prepopulated_fields = {'slug':('title', )}
    list_display = ('id','photo','title','slug','type','quantity', 'price', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'type__name']
    list_filter = ['type__name','is_published']
    save_on_top=True

    @admin.display(description='Фото')
    def photo(self, jewelry: Jewelry):
        if jewelry.image:
            return mark_safe(f"<img src='{jewelry.image.url}'width=50")
        else:
            return "None"


    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Jewelry.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять с публиковать выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Jewelry.Status.DRAFT)
        self.message_user(request, f'{count} записей сняты с публикации.', messages.WARNING)

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display=('id','name','image')
    list_display_links = ('id', 'name')

@admin.register(UploadFiles)
class UploadFilesAdmin(admin.ModelAdmin):
    list_display=('id','file')
    list_display_links=('id','file')
