# Generated by Django 4.2.3 on 2023-09-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='city',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
    ]