# Generated by Django 4.0.6 on 2022-07-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_espacos_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacos',
            name='imagem1',
            field=models.ImageField(blank=True, upload_to='fotos/espacos/imagem1'),
        ),
    ]