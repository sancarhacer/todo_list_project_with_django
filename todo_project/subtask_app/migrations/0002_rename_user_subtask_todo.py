# Generated by Django 5.0.6 on 2024-07-12 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subtask_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subtask',
            old_name='user',
            new_name='todo',
        ),
    ]
