# Generated by Django 4.1.2 on 2023-02-02 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0010_rename_behavior1_behavior_target_behavior_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='behaviorcheckin',
            old_name='behavior',
            new_name='target_behavior',
        ),
    ]
