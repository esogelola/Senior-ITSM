# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Contracts(models.Model):
    manf = models.TextField(db_column='Manf', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    expiry = models.DateField(db_column='Expiry', blank=True, null=True)  # Field name made lowercase.
    rowid = models.AutoField(db_column='RowID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contracts'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
