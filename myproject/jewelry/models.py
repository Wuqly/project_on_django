from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.

def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))

class PublishedManadger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Jewelry.Status.PUBLISHED) 

class Jewelry(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    image = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name='Фото №1')
    image_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name='Фото №2')
    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='Slug')
    type = models.ForeignKey('Types',on_delete=models.PROTECT, verbose_name='Тип изделия')
    quantity = models.IntegerField(verbose_name='Количество')
    price = models.CharField(max_length=50, verbose_name='Цена')
    type_metall = models.CharField(max_length=250, verbose_name='Тип металла',default=None, blank=True, null=True)
    weight = models.CharField(max_length=250, verbose_name='Вес',default=None, blank=True, null=True)
    size = models.CharField(max_length=250, verbose_name='Размер',default=None, blank=True, null=True)
    test = models.IntegerField(verbose_name='Проба',default=None, blank=True, null=True)
    description = models.CharField(max_length=400, verbose_name='Описание',default=None, blank=True, null=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                    default=Status.DRAFT, verbose_name='Статус')


    objects = models.Manager()
    published = PublishedManadger()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_slug': self.slug})

'''    
    def save(self, *args, **kwargs):
        self.slug = slugify(translit_to_eng(self.title))
        super().save(*args, **kwargs)
    '''

class Types(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Тип товаров'    

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'cat_slug': self.slug})
    

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')

    
    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'