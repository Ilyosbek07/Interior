# Generated by Django 3.2.3 on 2021-07-06 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_productmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogModel',
        ),
        migrations.DeleteModel(
            name='PostModel',
        ),
    ]
