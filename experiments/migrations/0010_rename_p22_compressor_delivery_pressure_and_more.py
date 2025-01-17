# Generated by Django 4.1.1 on 2023-03-16 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0009_compressor_pi1_compressor_v1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compressor',
            old_name='p22',
            new_name='Delivery_pressure',
        ),
        migrations.RenameField(
            model_name='compressor',
            old_name='pi1',
            new_name='power_input',
        ),
        migrations.RenameField(
            model_name='compressor',
            old_name='t1',
            new_name='pressure_head_cm',
        ),
        migrations.RenameField(
            model_name='compressor',
            old_name='v1',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='compressor',
            old_name='x1',
            new_name='volumetric_efficiency',
        ),
    ]