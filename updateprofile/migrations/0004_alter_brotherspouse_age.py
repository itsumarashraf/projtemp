# Generated by Django 3.2.9 on 2022-01-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updateprofile', '0003_alter_brotherspouse_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brotherspouse',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
