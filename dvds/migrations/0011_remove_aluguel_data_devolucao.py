# Generated by Django 4.1.7 on 2023-03-09 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dvds', '0010_aluguel_data_aluguel_aluguel_data_devolucao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluguel',
            name='data_devolucao',
        ),
    ]
