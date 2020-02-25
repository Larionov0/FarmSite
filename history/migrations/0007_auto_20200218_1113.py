# Generated by Django 2.2.7 on 2020-02-18 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0006_auto_20200218_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='change',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.ChangeType'),
        ),
    ]