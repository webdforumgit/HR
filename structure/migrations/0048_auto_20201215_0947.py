# Generated by Django 3.1.3 on 2020-12-15 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0047_auto_20201215_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 15, 9, 47, 8, 864564)),
        ),
    ]
