# Generated by Django 3.1.3 on 2020-12-14 03:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0040_auto_20201214_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 14, 9, 21, 22, 381953)),
        ),
    ]
