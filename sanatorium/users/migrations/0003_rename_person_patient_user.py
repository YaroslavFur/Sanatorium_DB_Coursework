# Generated by Django 4.0.4 on 2022-05-06 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_person_employee_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='person',
            new_name='user',
        ),
    ]
