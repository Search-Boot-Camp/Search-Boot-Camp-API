# Generated by Django 4.0.2 on 2022-02-03 00:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BootCamp', '0010_alter_bootcamp_accept_alter_bootcamp_apply_condition_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootcamp',
            name='count',
        ),
    ]
