# Generated by Django 5.0.6 on 2024-05-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_rename_actions_action_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='verb',
            field=models.CharField(max_length=255),
        ),
    ]