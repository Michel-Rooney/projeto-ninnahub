# Generated by Django 4.0.6 on 2022-07-29 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0009_alter_espacos_imagem1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='espacos',
            name='imagem1',
        ),
        migrations.AddField(
            model_name='espacos',
            name='imagem',
            field=models.ImageField(blank=True, default='default.png', upload_to='fotos/espacos %d-%m-%Y/imagem1'),
        ),
    ]