# Generated by Django 3.1.3 on 2020-12-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendence', '0004_auto_20201213_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date5', models.DateField(auto_now=True)),
            ],
        ),
    ]
