# Generated by Django 3.2 on 2021-08-10 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0006_alter_novel_bookimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapters',
            old_name='numnber',
            new_name='number',
        ),
    ]
