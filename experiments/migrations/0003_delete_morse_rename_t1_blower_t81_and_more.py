# Generated by Django 4.0.5 on 2022-06-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_bhpvilliers_blower_heatbalence_morse'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Morse',
        ),
        migrations.RenameField(
            model_name='blower',
            old_name='t1',
            new_name='t81',
        ),
        migrations.RenameField(
            model_name='compressor',
            old_name='t1',
            new_name='t71',
        ),
    ]