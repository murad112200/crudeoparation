# Generated by Django 5.1.6 on 2025-03-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
