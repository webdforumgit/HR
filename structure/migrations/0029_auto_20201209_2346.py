# Generated by Django 3.1.3 on 2020-12-09 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0028_auto_20201209_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeess',
            name='password',
            field=models.CharField(default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 9, 23, 46, 55, 987803)),
        ),
    ]
