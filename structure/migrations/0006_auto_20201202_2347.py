# Generated by Django 3.1.3 on 2020-12-02 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0005_auto_20201202_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='company_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 2, 23, 47, 8, 394680)),
        ),
    ]
