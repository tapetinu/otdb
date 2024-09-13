# Generated by Django 5.0.6 on 2024-09-12 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OsuUser',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=15)),
                ('avatar', models.CharField()),
                ('cover', models.CharField()),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
