# Generated by Django 2.0.6 on 2019-10-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0012_auto_20191005_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(default='not uploaded', upload_to=''),
        ),
    ]
