# Generated by Django 3.0.4 on 2020-03-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200312_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='minipc',
            name='optical_sensor',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='ram_extension',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='touchpad',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='trackpoint',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]