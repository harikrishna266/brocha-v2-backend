# Generated by Django 3.0.2 on 2020-01-12 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbx', '0003_auto_20200112_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fbx',
            name='fbx',
            field=models.FileField(blank=True, max_length=200, upload_to='images/designs'),
        ),
    ]
