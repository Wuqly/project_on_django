# Generated by Django 5.0.6 on 2024-07-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0003_alter_jewelry_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='is_published',
            field=models.BooleanField(choices=[(0, 'Черновик'), (1, 'Опубликовано')], default=0),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='quantity',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='type',
            field=models.CharField(max_length=250),
        ),
    ]
