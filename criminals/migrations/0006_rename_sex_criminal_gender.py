# Generated by Django 3.2.9 on 2021-12-09 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0005_auto_20211209_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criminal',
            old_name='sex',
            new_name='gender',
        ),
    ]
