# Generated by Django 4.0.4 on 2022-05-12 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperation', '0005_alter_hospital_bill'),
        ('users', '0009_employee_bill_alter_patient_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hospitals',
            field=models.ManyToManyField(blank=True, to='cooperation.hospital'),
        ),
    ]
