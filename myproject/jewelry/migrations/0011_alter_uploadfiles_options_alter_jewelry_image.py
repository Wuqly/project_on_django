# Generated by Django 5.0.6 on 2024-07-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0010_alter_jewelry_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadfiles',
            options={'verbose_name': 'Фотографии', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
