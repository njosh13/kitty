# Generated by Django 4.0.2 on 2022-03-08 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='userid',
            new_name='user',
        ),
    ]