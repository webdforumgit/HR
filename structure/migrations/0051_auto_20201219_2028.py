# Generated by Django 3.1.3 on 2020-12-19 14:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0050_auto_20201216_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 19, 20, 28, 55, 496158)),
        ),
    ]