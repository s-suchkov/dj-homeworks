# Generated by Django 2.1.3 on 2019-09-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20190920_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fields',
            name='width',
            field=models.IntegerField(),
        ),
    ]
