# Generated by Django 2.2.6 on 2019-11-01 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20191031_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestats',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Game'),
        ),
    ]
