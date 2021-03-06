# Generated by Django 3.0.4 on 2020-03-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200312_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='minipc',
            name='dvi',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='ethernet',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='vga',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='minipc',
            name='micro_hdmi',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='minipc',
            name='mini_hdmi',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
