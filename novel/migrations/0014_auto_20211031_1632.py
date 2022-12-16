# Generated by Django 3.2.7 on 2021-10-31 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0013_alter_groupchat_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='admins',
            field=models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='room',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
