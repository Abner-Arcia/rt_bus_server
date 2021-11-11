# Generated by Django 3.2 on 2021-11-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('route', models.JSONField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('creation_date', models.DateTimeField()),
            ],
        ),
    ]
