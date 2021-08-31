# Generated by Django 3.2 on 2021-08-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0008_auto_20210810_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='recently_viewed_novels',
        ),
        migrations.AddField(
            model_name='user',
            name='recently_viewed_novels',
            field=models.ManyToManyField(blank=True, null=True, related_name='recently_viewed_novels', to='novel.Novel'),
        ),
    ]
