# Generated by Django 2.1.1 on 2019-08-13 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_auto_20190814_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]
