# Generated by Django 3.1.3 on 2020-12-16 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20201215_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uplodaed_file',
            name='workflow_id_uplodaed_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflow_id_uplodaed_file', to='workflow.work_flow_employee_detail'),
        ),
    ]
