# Generated by Django 5.0.6 on 2024-05-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
    ]