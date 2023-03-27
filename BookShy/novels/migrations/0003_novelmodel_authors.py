# Generated by Django 4.1.7 on 2023-03-27 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('novels', '0002_rename_pubished_novelmodel_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='novelmodel',
            name='authors',
            field=models.ManyToManyField(null=True, related_name='books', to='authors.authormodel'),
        ),
    ]
