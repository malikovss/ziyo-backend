# Generated by Django 3.1.4 on 2021-01-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210101_1923'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TvProject',
            new_name='TvProgram',
        ),
    ]
