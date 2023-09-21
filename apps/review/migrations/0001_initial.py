# Generated by Django 4.2.3 on 2023-09-21 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5, verbose_name='Rating')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_barber', to='accounts.barber', verbose_name='Barber')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
