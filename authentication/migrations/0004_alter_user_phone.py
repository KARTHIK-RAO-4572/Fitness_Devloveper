# Generated by Django 5.0.6 on 2024-05-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
