# Generated by Django 2.2.7 on 2019-12-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20191202_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='special_marks',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]