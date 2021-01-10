# Generated by Django 3.1.5 on 2021-01-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_delete_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=32)),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
            ],
        ),
    ]
