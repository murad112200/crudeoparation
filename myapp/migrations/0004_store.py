# Generated by Django 5.1.6 on 2025-03-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_teacher_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('nunber', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
