# Generated by Django 3.2.23 on 2024-05-08 07:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20240506_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='Create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]