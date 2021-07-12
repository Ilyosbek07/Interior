# Generated by Django 3.2.3 on 2021-07-07 04:27

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, verbose_name='title')),
                ('title_en', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('title_uz', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=55, null=True, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AddField(
            model_name='postmodel',
            name='post_detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='post detail'),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='post.categorymodel', verbose_name='category'),
            preserve_default=False,
        ),
    ]