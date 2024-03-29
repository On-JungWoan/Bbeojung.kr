# Generated by Django 4.1.2 on 2022-10-30 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='i_congestion',
            old_name='i_con',
            new_name='con',
        ),
        migrations.RenameField(
            model_name='i_congestion',
            old_name='i',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='i_mean_sum',
            old_name='i_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='i_mean_sum',
            old_name='i_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='i_mean_sum',
            old_name='i',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='iw_mean_sum',
            old_name='iw_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='iw_mean_sum',
            old_name='iw_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='iw_mean_sum',
            old_name='iw',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='r_congestion',
            old_name='r_con',
            new_name='con',
        ),
        migrations.RenameField(
            model_name='r_congestion',
            old_name='r',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='r_mean_sum',
            old_name='r_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='r_mean_sum',
            old_name='r_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='r_mean_sum',
            old_name='r',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='ri_mean_sum',
            old_name='ri_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='ri_mean_sum',
            old_name='ri_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='ri_mean_sum',
            old_name='ri',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='riw_mean_sum',
            old_name='riw_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='riw_mean_sum',
            old_name='riw_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='riw_mean_sum',
            old_name='riw',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='rw_mean_sum',
            old_name='rw_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='rw_mean_sum',
            old_name='rw_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='rw_mean_sum',
            old_name='rw',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='w_congestion',
            old_name='w_con',
            new_name='con',
        ),
        migrations.RenameField(
            model_name='w_congestion',
            old_name='w',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='w_mean_sum',
            old_name='w_m',
            new_name='m',
        ),
        migrations.RenameField(
            model_name='w_mean_sum',
            old_name='w_s',
            new_name='s',
        ),
        migrations.RenameField(
            model_name='w_mean_sum',
            old_name='w',
            new_name='target',
        ),
    ]
