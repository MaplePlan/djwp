from django.db import models

# Create your models here.

from datetime import datetime

class Wlinks(models.Model):
	wurl = models.CharField(max_length=255)
	wname = models.CharField(max_length=255)
	wimage = models.CharField(max_length=255)
	wtarget = models.CharField(max_length=25)
	wdescription = models.CharField(max_length=255)
	wvisible = models.BooleanField(default=True)
	wowner = models.BigIntegerField(default=1)
	wrating = models.IntegerField(default=0)
	wupdated = models.DateTimeField(default=datetime.now())
	wrel = models.CharField(max_length=255)
	wnotes = models.TextField()
	wrss = models.CharField(max_length=255)

	def __unicode__(self):
		return self.wname

class Woptions(models.Model):
	wname = models.CharField(max_length=64)
	wvalue = models.TextField()
	wautoload = models.BooleanField(default=True)

	def __unicode__(self):
		return self.wname