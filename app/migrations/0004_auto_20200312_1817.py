# Generated by Django 3.0.4 on 2020-03-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200312_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='minipc',
            old_name='battery',
            new_name='battery_capacity',
        ),
        migrations.RenameField(
            model_name='minipc',
            old_name='ram',
            new_name='ram_technology',
        ),
        migrations.AddField(
            model_name='minipc',
            name='m2_slot_nvme',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='m2_slot_sata',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='ram_capacity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='minipc',
            name='storage_capacity',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='minipc',
            name='comment',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
