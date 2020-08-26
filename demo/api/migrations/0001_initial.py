# Generated by Django 3.1 on 2020-08-26 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('authid', models.CharField(max_length=18)),
                ('schoolname', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=32)),
                ('rename', models.CharField(max_length=64)),
                ('register_time', models.DateTimeField()),
                ('phone', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'master',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('designator', models.CharField(max_length=64)),
                ('fount', models.DateTimeField()),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.master')),
            ],
            options={
                'verbose_name': '班级',
                'verbose_name_plural': '班级',
                'db_table': 'grade',
            },
        ),
    ]