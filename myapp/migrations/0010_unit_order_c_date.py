# Generated by Django 5.0.2 on 2024-04-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_job_apply_address_job_apply_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit_order',
            name='c_date',
            field=models.CharField(default='', max_length=50),
        ),
    ]
