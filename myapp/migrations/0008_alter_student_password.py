# Generated by Django 5.1.6 on 2025-03-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_emil_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
