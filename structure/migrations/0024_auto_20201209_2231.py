# Generated by Django 3.1.3 on 2020-12-09 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0023_auto_20201209_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 22, 31, 57, 797082)),
        ),
    ]
