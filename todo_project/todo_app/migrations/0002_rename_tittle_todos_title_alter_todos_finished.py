# Generated by Django 5.0.6 on 2024-07-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todos',
            old_name='tittle',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='todos',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
