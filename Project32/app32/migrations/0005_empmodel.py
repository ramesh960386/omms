# Generated by Django 2.2.6 on 2019-11-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app32', '0004_auto_20191110_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpModel',
            fields=[
                ('Emp_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Email_ID', models.CharField(max_length=100)),
            ],
        ),
    ]
