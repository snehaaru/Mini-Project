# Generated by Django 3.2.16 on 2022-11-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Darshana',
            fields=[
                ('did', models.AutoField(primary_key=True, serialize=False)),
                ('day', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('specialpooja', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'darshana',
                'managed': False,
            },
        ),
    ]
