# Generated by Django 5.1.6 on 2025-03-11 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apptracker', '0002_apptracker_delete_todo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppTracker',
            new_name='Application',
        ),
    ]
