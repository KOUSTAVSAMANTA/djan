# Generated by Django 2.1.5 on 2021-04-02 07:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='learning_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 13, 11, 49, 964977), verbose_name='date published'),
        ),
    ]
