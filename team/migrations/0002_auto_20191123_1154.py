# Generated by Django 2.2.6 on 2019-11-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='legend',
            new_name='former',
        ),
    ]
