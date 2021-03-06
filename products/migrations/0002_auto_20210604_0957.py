# Generated by Django 3.2.3 on 2021-06-04 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caruselmodel',
            name='content_en',
            field=models.CharField(max_length=255, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='caruselmodel',
            name='content_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='caruselmodel',
            name='content_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='caruselmodel',
            name='title_en',
            field=models.CharField(max_length=25, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='caruselmodel',
            name='title_ru',
            field=models.CharField(max_length=25, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='caruselmodel',
            name='title_uz',
            field=models.CharField(max_length=25, null=True, verbose_name='title'),
        ),
    ]
