# Generated by Django 3.1.3 on 2020-12-16 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0008_auto_20201216_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uplodaed_file',
            name='emp_id_uplodaed_file',
        ),
    ]