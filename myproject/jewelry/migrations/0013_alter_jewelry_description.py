# Generated by Django 5.0.6 on 2024-07-22 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0012_jewelry_description_jewelry_size_jewelry_test_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=400, null=True, verbose_name='Описание'),
        ),
    ]
