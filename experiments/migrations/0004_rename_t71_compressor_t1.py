# Generated by Django 4.0.5 on 2022-06-30 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_delete_morse_rename_t1_blower_t81_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compressor',
            old_name='t71',
            new_name='t1',
        ),
    ]
