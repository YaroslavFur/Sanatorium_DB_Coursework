# Generated by Django 4.0.4 on 2022-05-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='last_change',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
