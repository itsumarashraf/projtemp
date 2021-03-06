# Generated by Django 3.2.9 on 2022-01-09 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('criminals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('criminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.criminal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='questionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('createdon', models.DateTimeField(auto_now_add=True)),
                ('updatedon', models.DateTimeField(auto_now=True)),
                ('criminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.criminal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
