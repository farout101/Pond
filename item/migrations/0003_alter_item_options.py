# Generated by Django 5.0.6 on 2024-05-29 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name'], 'verbose_name': 'item', 'verbose_name_plural': 'items'},
        ),
    ]
