# Generated by Django 4.1.2 on 2022-10-30 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='distance',
        ),
        migrations.DeleteModel(
            name='i_congestion',
        ),
        migrations.DeleteModel(
            name='i_mean_sum',
        ),
        migrations.DeleteModel(
            name='iw_mean_sum',
        ),
        migrations.DeleteModel(
            name='r_congestion',
        ),
        migrations.DeleteModel(
            name='r_mean_sum',
        ),
        migrations.DeleteModel(
            name='ri_mean_sum',
        ),
        migrations.DeleteModel(
            name='riw_mean_sum',
        ),
        migrations.DeleteModel(
            name='rw_mean_sum',
        ),
        migrations.DeleteModel(
            name='w_congestion',
        ),
        migrations.DeleteModel(
            name='w_mean_sum',
        ),
    ]
