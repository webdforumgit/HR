# Generated by Django 3.1.3 on 2020-12-05 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0019_auto_20201205_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 5, 20, 26, 5, 615771)),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='logo',
            field=models.ImageField(default='default_company_logo.jpg', upload_to='company_logo'),
        ),
    ]
