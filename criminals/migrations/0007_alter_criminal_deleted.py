# Generated by Django 3.2.9 on 2021-12-09 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0006_rename_sex_criminal_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='deleted',
            field=models.BooleanField(default=1),
        ),
    ]