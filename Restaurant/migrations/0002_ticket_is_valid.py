# Generated by Django 4.0.1 on 2022-01-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
    ]
