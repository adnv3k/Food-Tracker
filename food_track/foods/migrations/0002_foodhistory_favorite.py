# Generated by Django 4.0.4 on 2022-05-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodhistory',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]