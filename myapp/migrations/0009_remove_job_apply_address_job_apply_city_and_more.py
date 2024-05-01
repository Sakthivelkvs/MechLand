# Generated by Django 5.0.2 on 2024-04-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_loan_master_ins_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_apply',
            name='Address',
        ),
        migrations.AddField(
            model_name='job_apply',
            name='City',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='Hname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='Pin',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='Place',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='job_apply',
            name='State',
            field=models.CharField(default='', max_length=50),
        ),
    ]
