from django.db import models


class Hardware(models.Model):
    hostname = models.TextField(db_column='HostName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    osname = models.TextField(db_column='OSName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    osversion = models.TextField(db_column='OSVersion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    osmanf = models.TextField(db_column='OSManf', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    osconf = models.TextField(db_column='OSConf', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    owner1 = models.TextField(db_column='Owner1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    boottime = models.DateField(db_column='BootTime', blank=True, null=True)  # Field name made lowercase.
    manf = models.TextField(db_column='Manf', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    biosvers = models.TextField(db_column='BIOSVers', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timezone = models.TextField(db_column='TimeZone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    totphysmem = models.TextField(db_column='TotPhysMem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    availphysmem = models.TextField(db_column='AvailPhysMem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    domain = models.TextField(db_column='Domain', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    logonserver = models.TextField(db_column='LogonServer', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    transdate = models.DateField(db_column='TransDate', blank=True, null=True)  # Field name made lowercase.
    serial1 = models.TextField(db_column='Serial1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processors = models.TextField(db_column='Processors', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hotfixes = models.TextField(db_column='Hotfixes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rowid = models.AutoField(db_column='RowID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hardware'


class Software(models.Model):
    manf = models.TextField(db_column='Manf', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    user1 = models.TextField(db_column='User1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    device = models.TextField(db_column='Device', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    price = models.DecimalField(db_column='Price', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rowid = models.AutoField(db_column='RowID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'software'


class Contract(models.Model):
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    expiry = models.DateField(db_column='Expiry', blank=True, null=True)  # Field name made lowercase.
    rowid = models.AutoField(db_column='RowID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contracts'