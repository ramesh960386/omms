# Generated by Django 2.2.6 on 2019-11-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app32', '0007_auto_20191110_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='Facility',
            field=models.CharField(max_length=100),
        ),
    ]