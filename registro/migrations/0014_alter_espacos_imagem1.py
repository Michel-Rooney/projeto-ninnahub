# Generated by Django 4.0.6 on 2022-07-29 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0013_alter_espacos_imagem1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacos',
            name='imagem1',
            field=models.ImageField(blank=True, upload_to='fotos/espacos %d-%m-%Y %H:%M:%S/imagem1'),
        ),
    ]
