# Generated by Django 3.1.3 on 2020-12-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0002_auto_20201212_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='intime',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
