# Generated by Django 3.0.4 on 2020-03-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200312_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='minipc',
            name='length_m2_nvme_port',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]