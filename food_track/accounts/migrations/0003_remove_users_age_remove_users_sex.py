# Generated by Django 4.0.4 on 2022-04-29 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='age',
        ),
        migrations.RemoveField(
            model_name='users',
            name='sex',
        ),
    ]
