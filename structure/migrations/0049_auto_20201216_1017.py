# Generated by Django 3.1.3 on 2020-12-16 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0048_auto_20201215_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 16, 10, 17, 32, 146394)),
        ),
    ]
