# Generated by Django 4.2.2 on 2023-07-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postmind', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
