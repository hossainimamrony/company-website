# Generated by Django 3.2.21 on 2023-10-11 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='First_Name',
            new_name='Full_Name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='Last_Name',
        ),
    ]
