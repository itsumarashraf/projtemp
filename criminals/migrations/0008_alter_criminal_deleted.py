# Generated by Django 3.2.9 on 2021-12-09 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0007_alter_criminal_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='deleted',
            field=models.BooleanField(default=0),
        ),
    ]