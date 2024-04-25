# Generated by Django 5.0.2 on 2024-04-24 03:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_attendance_month_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(default='')),
                ('shift', models.CharField(default='', max_length=50)),
                ('unit', models.CharField(default='', max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.add_mould')),
            ],
        ),
    ]
