# Generated by Django 5.0.6 on 2024-07-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jewelry', '0004_alter_jewelry_is_published_alter_jewelry_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jewelry',
            name='type',
        ),
    ]
