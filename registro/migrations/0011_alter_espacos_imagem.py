# Generated by Django 4.0.6 on 2022-07-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0010_remove_espacos_imagem1_espacos_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacos',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='fotos/espacos %d-%m-%Y/imagem1'),
        ),
    ]
