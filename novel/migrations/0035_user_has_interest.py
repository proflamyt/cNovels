# Generated by Django 3.2.7 on 2022-03-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0034_auto_20220319_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_interest',
            field=models.BooleanField(default=False),
        ),
    ]
