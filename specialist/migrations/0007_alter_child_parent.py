# Generated by Django 4.1.5 on 2023-01-26 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0006_alter_child_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='parent',
            field=models.CharField(max_length=255),
        ),
    ]
