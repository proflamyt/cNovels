# Generated by Django 3.2.7 on 2021-11-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0023_auto_20211123_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recently_viewed_audios',
            field=models.ManyToManyField(blank=True, related_name='recently_viewed_audios', to='novel.Audio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='saved_audios',
            field=models.ManyToManyField(blank=True, related_name='saved_audios', to='novel.Audio'),
        ),
        migrations.AlterField(
            model_name='user',
            name='saved_poems',
            field=models.ManyToManyField(blank=True, related_name='saved_poems', to='novel.Poems'),
        ),
    ]
