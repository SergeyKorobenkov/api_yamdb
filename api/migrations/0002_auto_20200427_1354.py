# Generated by Django 3.0.5 on 2020-04-27 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='genre',
            new_name='genres',
        ),
    ]
