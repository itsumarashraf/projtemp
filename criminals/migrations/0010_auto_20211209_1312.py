# Generated by Django 3.2.9 on 2021-12-09 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0009_alter_criminal_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminal',
            name='status',
        ),
        migrations.AlterField(
            model_name='criminal',
            name='code',
            field=models.CharField(default='B98469', max_length=100),
        ),
    ]
