# Generated by Django 3.0.4 on 2020-03-12 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200312_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu',
            name='model',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]