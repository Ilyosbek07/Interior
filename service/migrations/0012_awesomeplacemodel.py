# Generated by Django 3.2.3 on 2021-07-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_delete_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwesomePlaceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='title')),
                ('title_en', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('content', models.CharField(max_length=255, verbose_name='content')),
                ('content_en', models.CharField(max_length=255, null=True, verbose_name='content')),
                ('content_uz', models.CharField(max_length=255, null=True, verbose_name='content')),
                ('content_ru', models.CharField(max_length=255, null=True, verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'awesome place',
                'verbose_name_plural': 'awesome places',
            },
        ),
    ]