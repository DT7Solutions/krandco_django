# Generated by Django 4.1 on 2024-03-22 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contactsubmit_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Tell_About_Project',
            new_name='About_Project',
        ),
    ]
