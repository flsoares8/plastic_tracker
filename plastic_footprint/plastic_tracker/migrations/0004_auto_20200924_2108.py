# Generated by Django 2.2.12 on 2020-09-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plastic_tracker', '0003_auto_20200924_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id_number',
            field=models.IntegerField(blank=True),
        ),
    ]
