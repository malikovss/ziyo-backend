# Generated by Django 3.1.4 on 2021-01-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210102_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
