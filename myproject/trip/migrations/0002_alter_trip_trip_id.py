# Generated by Django 5.0.2 on 2024-02-26 19:31

import trip.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(default=trip.models.generate_trip_id, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
