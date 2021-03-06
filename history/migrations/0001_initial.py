# Generated by Django 2.2.7 on 2020-02-13 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0004_auto_20191202_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('total_weight', models.FloatField(default=0)),
                ('description', models.CharField(default='', max_length=300)),
                ('animals', models.ManyToManyField(blank=True, null=True, to='info.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(default='', max_length=50)),
                ('change', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.Change')),
                ('from_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(default='', max_length=50)),
                ('change', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.Change')),
                ('to_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.Change')),
                ('from_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='all_moves_from', to='info.Cell')),
                ('to_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='all_moves_to', to='info.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('changes', models.ManyToManyField(blank=True, null=True, to='history.Change')),
            ],
        ),
        migrations.CreateModel(
            name='Die',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.Change')),
                ('from_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Cell')),
            ],
        ),
        migrations.CreateModel(
            name='Born',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='history.Change')),
                ('to_cell', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.Cell')),
            ],
        ),
    ]
