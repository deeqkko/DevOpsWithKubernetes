# Generated by Django 3.1.7 on 2021-05-21 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210405_0553'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Done'),
        ),
    ]
