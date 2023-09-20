# Generated by Django 4.2.3 on 2023-09-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_portfolio_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='accounts.barber', verbose_name='Barber'),
        ),
    ]