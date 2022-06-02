# Generated by Django 4.0.4 on 2022-05-29 18:19

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
                ('dong_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dist', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='congestion',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('r', models.CharField(blank=True, max_length=200, null=True)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('w', models.CharField(blank=True, max_length=200, null=True)),
                ('r_con', models.FloatField(blank=True, null=True)),
                ('i_con', models.FloatField(blank=True, null=True)),
                ('w_con', models.FloatField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='distance',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('dis_5159', models.FloatField(blank=True, null=True)),
                ('dis_5745', models.FloatField(blank=True, null=True)),
                ('dis_5445', models.FloatField(blank=True, null=True)),
                ('dis_4475', models.FloatField(blank=True, null=True)),
                ('dis_4406', models.FloatField(blank=True, null=True)),
                ('dis_2002', models.FloatField(blank=True, null=True)),
                ('dis_2232', models.FloatField(blank=True, null=True)),
                ('dis_6130', models.FloatField(blank=True, null=True)),
                ('dis_3236', models.FloatField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('r', models.CharField(blank=True, max_length=200, null=True)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('ri', models.CharField(blank=True, max_length=200, null=True)),
                ('riw', models.CharField(blank=True, max_length=200, null=True)),
                ('r_encode', models.IntegerField(blank=True, null=True)),
                ('i_encode', models.IntegerField(blank=True, null=True)),
                ('riw_encode', models.IntegerField(blank=True, null=True)),
                ('ri_encode', models.IntegerField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mean_sum',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('r', models.CharField(blank=True, max_length=200, null=True)),
                ('i', models.CharField(blank=True, max_length=200, null=True)),
                ('w', models.CharField(blank=True, max_length=200, null=True)),
                ('rw', models.CharField(blank=True, max_length=200, null=True)),
                ('ri', models.CharField(blank=True, max_length=200, null=True)),
                ('iw', models.CharField(blank=True, max_length=200, null=True)),
                ('riw', models.CharField(blank=True, max_length=200, null=True)),
                ('ri_m', models.FloatField(blank=True, null=True)),
                ('ri_s', models.FloatField(blank=True, null=True)),
                ('r_m', models.FloatField(blank=True, null=True)),
                ('r_s', models.FloatField(blank=True, null=True)),
                ('i_m', models.FloatField(blank=True, null=True)),
                ('i_s', models.FloatField(blank=True, null=True)),
                ('w_m', models.FloatField(blank=True, null=True)),
                ('w_s', models.FloatField(blank=True, null=True)),
                ('rw_m', models.FloatField(blank=True, null=True)),
                ('rw_s', models.FloatField(blank=True, null=True)),
                ('iw_m', models.FloatField(blank=True, null=True)),
                ('iw_s', models.FloatField(blank=True, null=True)),
                ('riw_m', models.FloatField(blank=True, null=True)),
                ('riw_s', models.FloatField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='population',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('dong_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dist', models.CharField(blank=True, max_length=200, null=True)),
                ('population', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]