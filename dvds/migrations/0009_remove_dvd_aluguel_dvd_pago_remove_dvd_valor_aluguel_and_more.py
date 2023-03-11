# Generated by Django 4.1.7 on 2023-03-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvds', '0008_aluguel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvd',
            name='aluguel_dvd_pago',
        ),
        migrations.RemoveField(
            model_name='dvd',
            name='valor_aluguel',
        ),
        migrations.AddField(
            model_name='aluguel',
            name='aluguel_dvd_pago',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aluguel',
            name='valor_aluguel',
            field=models.FloatField(default=0.0),
        ),
    ]
