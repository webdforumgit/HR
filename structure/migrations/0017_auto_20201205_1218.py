# Generated by Django 3.1.3 on 2020-12-05 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0016_auto_20201205_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_details',
            name='company_name',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 12, 18, 23, 964575)),
        ),
    ]
