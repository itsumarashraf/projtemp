# Generated by Django 3.2.9 on 2022-01-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0006_alter_criminal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='code',
            field=models.CharField(default='596DC6', max_length=100),
        ),
    ]