# Generated by Django 3.1.7 on 2021-04-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20210405_0539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potd',
            name='image_file',
            field=models.ImageField(upload_to='potd'),
        ),
    ]
