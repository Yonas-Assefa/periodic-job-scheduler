# Generated by Django 4.2.16 on 2024-09-17 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='script',
            old_name='name',
            new_name='script_name',
        ),
    ]
