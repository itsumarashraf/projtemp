# Generated by Django 3.2.9 on 2021-12-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0012_alter_criminal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criminal',
            name='code',
            field=models.CharField(default='D45C01', max_length=100),
        ),
    ]