# Generated by Django 4.2.3 on 2023-09-20 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_barber_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='portfolio/', verbose_name='File')),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.barber', verbose_name='Barber')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
            },
        ),
    ]
