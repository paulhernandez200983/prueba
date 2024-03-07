# Generated by Django 5.0.2 on 2024-02-24 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_remove_chicken1_lat_remove_chicken1_lon'),
    ]

    operations = [
        migrations.AddField(
            model_name='chicken1',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=23.634501, max_digits=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chicken1',
            name='lon',
            field=models.DecimalField(decimal_places=6, default=-102.552784, max_digits=12),
            preserve_default=False,
        ),
    ]
