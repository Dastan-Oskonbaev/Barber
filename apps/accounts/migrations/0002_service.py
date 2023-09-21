# Generated by Django 4.2.3 on 2023-09-21 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('barber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='accounts.barber', verbose_name='Barber')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]