# Generated by Django 4.0.2 on 2022-02-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootCamp', '0011_remove_bootcamp_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamp',
            name='apply_end',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bootcamp',
            name='apply_start',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
