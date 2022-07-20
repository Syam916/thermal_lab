# Generated by Django 4.0.5 on 2022-07-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0005_delete_bhpvilliers_delete_blower_delete_heatbalence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bhpvilliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L1', models.CharField(max_length=10)),
                ('X1', models.CharField(max_length=10)),
                ('T1', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Blower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1', models.CharField(max_length=10)),
                ('d1', models.CharField(max_length=10)),
                ('T1', models.CharField(max_length=10)),
                ('t81', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Heatbalence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('L1', models.CharField(max_length=10)),
                ('X1', models.CharField(max_length=10)),
                ('T11', models.CharField(max_length=10)),
                ('T111', models.CharField(max_length=10)),
                ('T22', models.CharField(max_length=10)),
                ('Q1', models.CharField(max_length=10)),
                ('T33', models.CharField(max_length=10)),
                ('T44', models.CharField(max_length=10)),
            ],
        ),
    ]