# Generated by Django 3.2.9 on 2022-01-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0005_alter_criminal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='code',
            field=models.CharField(default='3BA8DF', max_length=100),
        ),
    ]
