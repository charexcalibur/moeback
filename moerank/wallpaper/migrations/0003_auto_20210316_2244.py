# Generated by Django 3.0.8 on 2021-03-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallpaper', '0002_auto_20210305_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='raw_url',
            field=models.URLField(blank=True, default='', null=True, unique=True, verbose_name='raw 地址'),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='thumbnail_url',
            field=models.URLField(blank=True, default='', null=True, unique=True, verbose_name='缩略图地址'),
        ),
        migrations.AlterField(
            model_name='wallpaper',
            name='wallpaper_url',
            field=models.URLField(blank=True, default='', null=True, unique=True, verbose_name='壁纸地址'),
        ),
    ]
