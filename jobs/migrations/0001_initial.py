# Generated by Django 4.2.16 on 2024-09-15 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('schedule_days', models.JSONField()),
                ('schedule_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('table_name', models.CharField(max_length=255)),
                ('order_exec', models.PositiveIntegerField()),
                ('import_enabled', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scripts', to='jobs.job')),
            ],
            options={
                'ordering': ['order_exec'],
            },
        ),
    ]
