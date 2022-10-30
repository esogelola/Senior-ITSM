from django.db import models
from django.contrib.auth.models import User


class Hardware(models.Model):
    HostName = models.CharField(max_length=100)
    OSName = models.CharField(max_length=100)
    OSVersion = models.CharField(max_length=100)
    OSManf = models.CharField(max_length=100)
    OSConf = models.CharField(max_length=100)
    Owner = models.CharField(max_length=100)
    BootTime = models.DateTimeField()
    Manf = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    BIOSVers = models.CharField(max_length=100)
    TimeZone = models.CharField(max_length=100)
    TotPhysMem = models.IntegerField()
    AvailPhysMem = models.IntegerField()
    Domain = models.CharField(max_length=100)
    LogonServer = models.CharField(max_length=100)
    TransDate = models.DateTimeField()
    Serial = models.CharField(max_length=100)
    Processors: models.CharField(max_length=100)
    Hotfixes = models.CharField(max_length=100)

    def __str__(self):
        return self.HostName


class Other(models.Model):
    Manf = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Expiry = models.DateTimeField()


class Software(models.Model):
    Manf = models.CharField(max_length=100)
    Title = models.CharField(max_length=100)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Device = models.DateTimeField()
    Price = models.IntegerField()
