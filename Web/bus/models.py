from django.db import models

#mean_sum
class r_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    r = models.CharField(max_length=200, blank=True, null=True)
    r_m = models.FloatField(blank=True, null=True)
    r_s = models.FloatField(blank=True, null=True)

class i_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    i = models.CharField(max_length=200, blank=True, null=True)
    i_m = models.FloatField(blank=True, null=True)
    i_s = models.FloatField(blank=True, null=True)

class w_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    w = models.CharField(max_length=200, blank=True, null=True)
    w_m = models.FloatField(blank=True, null=True)
    w_s = models.FloatField(blank=True, null=True)

class ri_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    ri = models.CharField(max_length=200, blank=True, null=True)
    ri_m = models.FloatField(blank=True, null=True)
    ri_s = models.FloatField(blank=True, null=True)

class rw_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    rw = models.CharField(max_length=200, blank=True, null=True)
    rw_m = models.FloatField(blank=True, null=True)
    rw_s = models.FloatField(blank=True, null=True)

class iw_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    iw = models.CharField(max_length=200, blank=True, null=True)
    iw_m = models.FloatField(blank=True, null=True)
    iw_s = models.FloatField(blank=True, null=True)

class riw_mean_sum(models.Model):
    idx = models.AutoField(primary_key=True)
    riw = models.CharField(max_length=200, blank=True, null=True)
    riw_m = models.FloatField(blank=True, null=True)
    riw_s = models.FloatField(blank=True, null=True)


#congestion
class i_congestion(models.Model):
    idx = models.AutoField(primary_key=True)
    i = models.CharField(max_length=200, blank=True, null=True)
    i_con = models.FloatField(blank=True, null=True)

class r_congestion(models.Model):
    idx = models.AutoField(primary_key=True)
    r = models.CharField(max_length=200, blank=True, null=True)
    r_con = models.FloatField(blank=True, null=True)

class w_congestion(models.Model):
    idx = models.AutoField(primary_key=True)
    w = models.CharField(max_length=200, blank=True, null=True)
    w_con = models.FloatField(blank=True, null=True)


class distance(models.Model):
    idx = models.AutoField(primary_key=True)
    i = models.CharField(max_length=200, blank=True, null=True)

    dis_0 = models.FloatField(blank=True, null=True)
    dis_1 = models.FloatField(blank=True, null=True)
    dis_2 = models.FloatField(blank=True, null=True)
    dis_3 = models.FloatField(blank=True, null=True)
    dis_4 = models.FloatField(blank=True, null=True)
    dis_5 = models.FloatField(blank=True, null=True)
    dis_6 = models.FloatField(blank=True, null=True)
    dis_7 = models.FloatField(blank=True, null=True)
    dis_8 = models.FloatField(blank=True, null=True)

    time = models.CharField(max_length=200, blank=True, null=True)


# class Label(models.Model):
#     idx = models.AutoField(primary_key=True)
#     r = models.CharField(max_length=200, blank=True, null=True)
#     i = models.CharField(max_length=200, blank=True, null=True)
#     riw = models.CharField(max_length=200, blank=True, null=True)
#     ri = models.CharField(max_length=200, blank=True, null=True)
#
#
#     r_encode = models.IntegerField(blank=True, null=True)
#     i_encode = models.IntegerField(blank=True, null=True)
#     riw_encode = models.IntegerField(blank=True, null=True)
#     ri_encode = models.IntegerField(blank=True, null=True)
#
#     time = models.CharField(max_length=200, blank=True, null=True)


class BusInfo(models.Model):
    idx = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    i = models.CharField(max_length=200, blank=True, null=True)
    r = models.CharField(max_length=200, blank=True, null=True)
    Lati = models.FloatField(blank=True, null=True)
    Longi = models.FloatField(blank=True, null=True)
    dong_name = models.CharField(max_length=200, blank=True, null=True)
    dist = models.CharField(max_length=200, blank=True, null=True)
    population = models.FloatField(blank=True, null=True)






