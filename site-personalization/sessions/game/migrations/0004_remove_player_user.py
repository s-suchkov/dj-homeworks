# Generated by Django 2.1.1 on 2019-09-06 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190907_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
    ]
