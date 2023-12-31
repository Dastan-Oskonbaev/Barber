# Generated by Django 4.2.3 on 2023-09-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='blog',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='description',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='description',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='description',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='description',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]
