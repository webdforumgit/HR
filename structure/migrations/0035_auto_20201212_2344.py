# Generated by Django 3.1.3 on 2020-12-12 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0034_auto_20201212_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 12, 23, 44, 0, 863448)),
        ),
    ]
