# Generated by Django 4.1.2 on 2022-10-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusInfo',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('r', models.CharField(blank=True, max_length=200, null=True)),
                ('Lati', models.FloatField(blank=True, null=True)),
                ('Longi', models.FloatField(blank=True, null=True)),
                ('dong_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dist', models.CharField(blank=True, max_length=200, null=True)),
                ('population', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='distance',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('dis_0', models.FloatField(blank=True, null=True)),
                ('dis_1', models.FloatField(blank=True, null=True)),
                ('dis_2', models.FloatField(blank=True, null=True)),
                ('dis_3', models.FloatField(blank=True, null=True)),
                ('dis_4', models.FloatField(blank=True, null=True)),
                ('dis_5', models.FloatField(blank=True, null=True)),
                ('dis_6', models.FloatField(blank=True, null=True)),
                ('dis_7', models.FloatField(blank=True, null=True)),
                ('dis_8', models.FloatField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_congestion',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('con', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='i_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='iw_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='r_congestion',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('con', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='r_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ri_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='riw_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rw_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='w_congestion',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('con', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='w_mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('target', models.CharField(blank=True, max_length=200, null=True)),
                ('m', models.FloatField(blank=True, null=True)),
                ('s', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
