# Generated by Django 3.1.5 on 2021-01-05 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_location_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='Name',
            field=models.CharField(default='Dhaka', max_length=32),
        ),
    ]
