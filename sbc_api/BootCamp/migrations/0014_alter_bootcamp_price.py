# Generated by Django 4.0.2 on 2022-02-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BootCamp', '0013_alter_bootcamp_bootcamp_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootcamp',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
