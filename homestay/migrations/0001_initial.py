# Generated by Django 4.0.1 on 2022-01-14 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homestay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField(null=True)),
                ('location', models.CharField(max_length=200)),
                ('guest', models.IntegerField()),
                ('bed', models.IntegerField()),
                ('bath', models.IntegerField()),
                ('wifi', models.IntegerField()),
                ('pool', models.IntegerField()),
                ('parking', models.IntegerField()),
            ],
        ),
    ]
