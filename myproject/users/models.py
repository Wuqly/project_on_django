from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone_number = models.CharField(blank=True, null=True,max_length=12, verbose_name='Номер телефона')
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
