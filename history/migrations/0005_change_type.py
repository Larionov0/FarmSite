# Generated by Django 2.2.7 on 2020-02-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_auto_20200218_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='change',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]
