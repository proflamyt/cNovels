# Generated by Django 3.2.7 on 2021-10-25 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0012_auto_20211025_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='novel.event'),
        ),
    ]