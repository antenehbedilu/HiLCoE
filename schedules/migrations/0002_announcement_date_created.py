# Generated by Django 2.1 on 2019-11-09 06:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]