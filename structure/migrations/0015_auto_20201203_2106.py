# Generated by Django 3.1.3 on 2020-12-03 15:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0014_auto_20201203_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_details',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 3, 21, 6, 37, 608528)),
        ),
        migrations.CreateModel(
            name='Company_uuids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('authenticated', models.BooleanField(default=False, max_length=100)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_id', to='structure.company_details')),
            ],
        ),
        migrations.CreateModel(
            name='Branche_uuids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=100)),
                ('authenticated', models.BooleanField(default=False, max_length=100)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_id', to='structure.branches')),
            ],
        ),
    ]