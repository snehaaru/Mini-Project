# Generated by Django 3.2.16 on 2022-11-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=500)),
                ('report', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'report',
                'managed': False,
            },
        ),
    ]