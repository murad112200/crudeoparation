# Generated by Django 5.1.6 on 2025-02-27 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('passord', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=20)),
                ('emil', models.EmailField(max_length=20)),
            ],
        ),
    ]
