# Generated by Django 2.1.3 on 2019-09-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20190920_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path_csv',
            name='file',
            field=models.FileField(upload_to='C:\\Users\\1\\Desktop\\django homework\\dj-homeworks\\creating-project\\application\\phones.csv'),
        ),
    ]
