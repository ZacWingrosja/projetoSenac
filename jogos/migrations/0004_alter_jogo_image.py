# Generated by Django 5.0.6 on 2024-07-03 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogos', '0003_alter_jogo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='template/assets/imagens'),
        ),
    ]
