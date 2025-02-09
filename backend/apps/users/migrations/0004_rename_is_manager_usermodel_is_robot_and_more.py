# Generated by Django 4.2.17 on 2025-01-27 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='is_manager',
            new_name='is_robot',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='is_supervisor',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usermodel',
            name='user_permissions',
        ),
    ]
