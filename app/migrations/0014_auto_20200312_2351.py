# Generated by Django 3.0.4 on 2020-03-12 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20200312_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='minipc',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]