# Generated by Django 5.0.2 on 2024-04-18 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_mould',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=50)),
                ('mtype', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('stock', models.CharField(default='', max_length=100)),
                ('size_type', models.CharField(default='', max_length=100)),
                ('size1', models.CharField(default='', max_length=100)),
                ('size2', models.CharField(default='', max_length=100)),
                ('size3', models.CharField(default='', max_length=100)),
                ('size', models.CharField(default='', max_length=100)),
                ('photo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'add_mould',
            },
        ),
        migrations.CreateModel(
            name='business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Company_name', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=150)),
                ('Comments', models.CharField(max_length=150)),
                ('date', models.CharField(default='', max_length=50)),
                ('time', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'business',
            },
        ),
        migrations.CreateModel(
            name='job_master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('job_role', models.CharField(max_length=50)),
                ('basic_salary', models.CharField(max_length=50)),
                ('allowance', models.CharField(max_length=50)),
                ('loan_allowance', models.CharField(max_length=50)),
                ('cut_salary', models.CharField(max_length=50)),
                ('requirements', models.CharField(default='', max_length=50)),
                ('vacancies', models.CharField(default='', max_length=50)),
                ('qualifications', models.CharField(default='', max_length=50)),
                ('experiences', models.CharField(default='', max_length=50)),
                ('date', models.DateField()),
                ('status', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'job_master',
            },
        ),
        migrations.CreateModel(
            name='leave_master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(max_length=50)),
                ('leave_limit', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'leave_master',
            },
        ),
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_amount', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=200)),
                ('initial_amount', models.CharField(default='', max_length=50)),
                ('installment', models.CharField(default='', max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'loan',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('house_name', models.CharField(default='', max_length=150)),
                ('Place', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(default='', max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='predict_mould',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mldname', models.CharField(max_length=50)),
                ('photo1', models.ImageField(upload_to='photos/')),
                ('photo2', models.ImageField(upload_to='photos/')),
                ('photo3', models.ImageField(upload_to='photos/')),
            ],
            options={
                'db_table': 'predict_mould',
            },
        ),
        migrations.CreateModel(
            name='shift',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shift_nbr', models.CharField(max_length=30)),
                ('shift_time', models.TimeField()),
            ],
            options={
                'db_table': 'shift',
            },
        ),
        migrations.CreateModel(
            name='uint_registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Company_Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Place', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(default='', max_length=100)),
                ('Pincode', models.CharField(max_length=100)),
                ('Photo', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'unit_registration',
            },
        ),
        migrations.CreateModel(
            name='job_apply',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Address', models.CharField(default='', max_length=150)),
                ('Photo', models.CharField(default='', max_length=200)),
                ('qualifications', models.CharField(max_length=50)),
                ('experiences', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=100)),
                ('int_date', models.CharField(default='', max_length=200)),
                ('int_time', models.CharField(default='', max_length=200)),
                ('venue', models.CharField(default='', max_length=200)),
                ('int_status', models.CharField(default='', max_length=200)),
                ('resume', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='', max_length=200)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.job_master')),
            ],
            options={
                'db_table': 'job_apply',
            },
        ),
        migrations.CreateModel(
            name='ratting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=50)),
                ('p1_ratting', models.IntegerField()),
                ('p2_ratting', models.IntegerField()),
                ('p3_ratting', models.IntegerField()),
                ('suggestion', models.CharField(max_length=200)),
                ('predict_mould_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.predict_mould')),
            ],
            options={
                'db_table': 'ratting',
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Date_of_birth', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=100)),
                ('Address', models.CharField(default='', max_length=150)),
                ('join_date', models.CharField(default='', max_length=50)),
                ('remark', models.CharField(default='', max_length=100)),
                ('section', models.CharField(default='', max_length=50)),
                ('Photo', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.job_master')),
            ],
            options={
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='shift_allotment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50)),
                ('shift_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.shift')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'shift_allotment',
            },
        ),
        migrations.CreateModel(
            name='shift_allot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('supervisor_id', models.CharField(default='', max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'shift_allot',
            },
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(default='', max_length=50)),
                ('leave', models.CharField(max_length=50)),
                ('leaveamount', models.CharField(max_length=50)),
                ('loan', models.CharField(max_length=50)),
                ('advance', models.CharField(max_length=50)),
                ('net_salary', models.CharField(max_length=50)),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(default='', max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'salary',
            },
        ),
        migrations.CreateModel(
            name='loan_master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('approval_date', models.CharField(max_length=50)),
                ('installment', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.loan')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'loan_master',
            },
        ),
        migrations.AddField(
            model_name='loan',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff'),
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('req_date', models.CharField(max_length=50)),
                ('laeve_date', models.CharField(max_length=50)),
                ('no_of_days', models.IntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=50)),
                ('leave_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.leave_master')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'Leave',
            },
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('no_of_working_days', models.CharField(max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='advance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('month', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.staff')),
            ],
            options={
                'db_table': 'advance',
            },
        ),
        migrations.CreateModel(
            name='unit_complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.uint_registration')),
            ],
            options={
                'db_table': 'unit_complaint',
            },
        ),
        migrations.CreateModel(
            name='unit_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(max_length=50)),
                ('size', models.CharField(default='', max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('delivary_date', models.CharField(default='', max_length=50)),
                ('delivary_time', models.CharField(default='', max_length=50)),
                ('remarks', models.CharField(default='', max_length=50)),
                ('payment_method', models.CharField(default='', max_length=50)),
                ('mould_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.add_mould')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.uint_registration')),
            ],
            options={
                'db_table': 'unit_order',
            },
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Account_num', models.CharField(max_length=50)),
                ('bank', models.CharField(max_length=50)),
                ('ifsc', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('unit_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.unit_order')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='cancel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.unit_order')),
            ],
            options={
                'db_table': 'cancel',
            },
        ),
        migrations.CreateModel(
            name='unit_review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=50)),
                ('mould_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.add_mould')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.uint_registration')),
            ],
            options={
                'db_table': 'unit_review',
            },
        ),
        migrations.CreateModel(
            name='unit_review1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=50)),
                ('mould_id1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.add_mould')),
                ('unit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.uint_registration')),
            ],
            options={
                'db_table': 'unit_review1',
            },
        ),
    ]