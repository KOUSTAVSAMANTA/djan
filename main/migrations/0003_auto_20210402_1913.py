# Generated by Django 2.1.5 on 2021-04-02 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210402_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='learning_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 19, 13, 41, 276616), verbose_name='date published'),
        ),
    ]