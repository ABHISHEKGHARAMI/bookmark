# Generated by Django 5.0.6 on 2024-05-29 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_form',
            new_name='user_from',
        ),
    ]
