# Generated by Django 3.0.8 on 2020-09-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, to='common.Role', verbose_name='角色'),
        ),
    ]
