from django.db import models

# Create your models here.

from datetime import datetime

class Wlink(models.Model):
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

class Woption(models.Model):
	wname = models.CharField(max_length=64)
	wvalue = models.TextField()
	wautoload = models.BooleanField(default=True)

	def __unicode__(self):
		return self.wname

class Wuser(models.Model):
	wusername = models.CharField(max_length=60)
	wpassword = models.CharField(max_length=64)
	wnickname = models.CharField(max_length=50)
	wemail = models.CharField(max_length=100)
	wuserurl = models.CharField(max_length=100)
	wregisteredtime = models.DateTimeField(default=datetime.now())
	wactivationkey = models.CharField(max_length=60)
	wstatus = models.IntegerField(default=0)
	wdisplayname = models.CharField(max_length=255)

	def __unicode__(self):
		return self.wusername

class Wusermeta(models.Model):
	wuser = models.ForeignKey(Wuser)
	wmetakey = models.CharField(max_length=255, default='')
	wmetavalue = models.TextField(default='')

	def __unicode__(self):
		return self.wmetakey

class Wterm(models.Model):
	wname = models.CharField(max_length=200)
	wslug = models.CharField(max_length=200)
	wtermgroup = models.BigIntegerField(default=0)

	def __unicode__(self):
		return self.wname

class Wtermtaxonomy(models.Model):
	wterm = models.ForeignKey(Wterm)
	wtaxonomy = models.CharField(max_length=32)
	wdescription = models.TextField()
	wparent = models.BigIntegerField(default=0)
	wcount = models.BigIntegerField(default=0)

	def __unicode__(self):
		return self.wtaxonomy

class Wtermrelationship(models.Model):
	wtermtaxonomy = models.ForeignKey(Wtermtaxonomy)
	wtermorder = models.IntegerField(default=0)

	def __unicode__(self):
		return self.wtermorder

class Wpost(models.Model):
	wauthor = models.ForeignKey(Wuser)
	wpostdate = models.DateTimeField(default=datetime.now())
	wpostdategmt = models.DateTimeField(default=datetime.now())
	wcontent = models.TextField()
	wtitle = models.TextField()
	wexcerpt = models.TextField()
	wstatus = models.CharField(max_length=20, default='publish')
	wcommentstatus = models.CharField(max_length=20, default='open')
	wpingstatus = models.CharField(max_length=20, default='open')
	wpostpassword = models.CharField(max_length=20)
	wpostname = models.CharField(max_length=200)
	wtoping = models.TextField()
	wpinged = models.TextField()
	wpostmodified = models.DateTimeField(default=datetime.now())
	wpostmodifiedgmt = models.DateTimeField(default=datetime.now())
	wcontentfiltered = models.TextField()
	wpostparent = models.ForeignKey('self', default=0)
	wguid = models.CharField(max_length=255)
	wmenuorder = models.IntegerField(default=0)
	wposttype = models.CharField(max_length=20)
	wpostmimetype = models.CharField(max_length=100)
	wcommentcount = models.BigIntegerField(default=0)

	def __unicode__(self):
		return self.wtitle

class Wpostmeta(models.Model):
	wpost = models.ForeignKey(Wpost)
	wmetakey = models.CharField(max_length=255)
	wmetavalue = models.TextField()

	def __unicode__(self):
		return self.wmetakey

class Wcomment(models.Model):
	wpost = models.ForeignKey(Wpost, default=0)
	wcommentauthor = models.TextField()
	wcommentauthoremai = models.CharField(max_length=100)
	wcommentauthorurl = models.CharField(max_length=200)
	wcommentauthorip = models.CharField(max_length=100)
	wcommenttime = models.DateTimeField(default=datetime.now())
	wcommentcontent = models.TextField()
	wcommentkarma = models.IntegerField(default=0)
	wcommentapproved = models.CharField(max_length=20, default='')
	wcommentagent = models.CharField(max_length=255)
	wcommenttype = models.CharField(max_length=20)
	wcommentparent = models.ForeignKey('self', default=0)
	wuser = models.ForeignKey(Wuser, default=0)

	def __unicode__(self):
		return self.wcommentauthor

class Wcommentmeta(models.Model):
	wcomment = models.ForeignKey(Wcomment, default=0)
	wmetakey = models.CharField(max_length=255)
	wmetavalue = models.TextField()





























	