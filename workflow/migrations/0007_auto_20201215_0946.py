# Generated by Django 3.1.3 on 2020-12-15 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0006_auto_20201214_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uplodaed_file',
            name='workflow_id_uplodaed_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workflow_id_uplodaed_file', to='workflow.work_flow'),
        ),
    ]
