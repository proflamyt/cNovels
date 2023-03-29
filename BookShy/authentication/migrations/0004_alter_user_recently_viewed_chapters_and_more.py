# Generated by Django 4.1.7 on 2023-03-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_genre_novelmodel_genre'),
        ('authentication', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='recently_viewed_chapters',
            field=models.ManyToManyField(blank=True, related_name='recently_viewed_chapters', to='novels.chaptermodel'),
        ),
        migrations.AlterField(
            model_name='user',
            name='saved_novels',
            field=models.ManyToManyField(blank=True, related_name='saved_novel', to='novels.novelmodel'),
        ),
    ]