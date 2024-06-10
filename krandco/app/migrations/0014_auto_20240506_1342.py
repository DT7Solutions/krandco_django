# Generated by Django 3.2.23 on 2024-05-06 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rename_volumes_productitem_volume_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitem',
            options={'ordering': ['-Create_at']},
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Chloride',
            new_name='CreatedName',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Colour',
            new_name='Grade',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Filling_Value',
            new_name='Packing',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Leaf_Size',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Marketing',
            new_name='Quantity',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Planting',
            new_name='Sugar',
        ),
        migrations.RenameField(
            model_name='productitem',
            old_name='Reducing_Sugars',
            new_name='Type',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='Volume',
        ),
        migrations.AddField(
            model_name='productitem',
            name='Create_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]