from django.conf import settings
from django.db import models
from django.db.models.functions import datetime
from django.utils import timezone


# Create your models here.
class Parceline(models.Model):
    ipaddr = models.CharField(max_length=20)
    dtimefield = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now, blank=True)
    httpmethod = models.CharField(max_length=8, blank=True)
    urlrequest = models.TextField(blank=True)
    responsecode = models.CharField(max_length=20, blank=True)
    bytesread = models.BigIntegerField(default=0)

