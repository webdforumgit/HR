# Generated by Django 3.0.5 on 2021-02-01 13:42

import attendence.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0055_auto_20210201_1912'),
        ('attendence', '0006_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence_sample_video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=attendence.models.content_file_name)),
                ('employee_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_id_wise_video', to='structure.Employeess')),
            ],
        ),
    ]
