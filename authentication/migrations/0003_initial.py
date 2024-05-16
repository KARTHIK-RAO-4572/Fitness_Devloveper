# Generated by Django 5.0.6 on 2024-05-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_delete_user'),
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
