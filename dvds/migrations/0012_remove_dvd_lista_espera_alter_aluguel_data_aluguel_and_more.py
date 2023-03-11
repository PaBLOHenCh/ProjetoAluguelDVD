# Generated by Django 4.1.7 on 2023-03-09 20:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dvds', '0011_remove_aluguel_data_devolucao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvd',
            name='lista_espera',
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='data_aluguel',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 9, 17, 4, 31, 579595)),
        ),
        migrations.CreateModel(
            name='lista_espera',
            fields=[
                ('id_dvd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dvds.dvd')),
                ('nome', models.CharField(max_length=255)),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
