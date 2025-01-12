# Generated by Django 4.2.17 on 2025-01-12 12:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
