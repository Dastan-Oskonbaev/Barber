# Generated by Django 4.2.3 on 2023-09-20 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_barber_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='barber/', verbose_name='Photo'),
        ),
    ]
