# Generated by Django 3.2.16 on 2022-11-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Festives',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('startsdate', models.CharField(max_length=20)),
                ('enddate', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=500)),
                ('spclpooja', models.CharField(max_length=500)),
                ('opentime', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'festives',
                'managed': False,
            },
        ),
    ]