# Generated by Django 4.0.4 on 2022-04-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nutrients', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'foods',
            },
        ),
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nutrients', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'nutrients',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
