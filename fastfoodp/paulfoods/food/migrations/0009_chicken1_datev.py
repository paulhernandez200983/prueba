# Generated by Django 5.0.2 on 2024-02-24 02:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_chicken1_estd'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicken1',
            name='datev',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
