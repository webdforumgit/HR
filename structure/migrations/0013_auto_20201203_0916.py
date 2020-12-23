# Generated by Django 3.1.3 on 2020-12-03 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0012_auto_20201203_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='company',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='company_user_email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 9, 16, 47, 565820)),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='max_accesable_uuid_no',
            field=models.CharField(default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='company_details',
            name='primary_uuid',
            field=models.TextField(max_length=360),
        ),
    ]