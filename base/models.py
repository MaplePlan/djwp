#coding=utf-8

from django.db import models

# Create your models here.

from datetime import datetime

class Wlink(models.Model):
	wid  = models.AutoField(primary_key=True, db_column='link_id')
	wurl = models.CharField(max_length=255, db_column='link_url')
	wname = models.CharField(max_length=255, db_column='link_name')
	wimage = models.CharField(max_length=255, db_column='link_image')
	wtarget = models.CharField(max_length=25, db_column='link_target')
	wdescription = models.CharField(max_length=255, db_column='link_description')
	wvisible = models.CharField(max_length='20', default='Y', db_column='link_visible')
	wowner = models.BigIntegerField(default=1, db_column='link_owner')
	wrating = models.IntegerField(default=0, db_column='link_rating')
	wupdated = models.DateTimeField(default=datetime.now(), db_column='link_updated')
	wrel = models.CharField(max_length=255, db_column='link_rel')
	wnotes = models.TextField(db_column='link_notes')
	wrss = models.CharField(max_length=255, db_column='link_rss')

	class Meta:
		db_table = 'wp_links'

	def __unicode__(self):
		return self.wname

class Woption(models.Model):
	wid = models.AutoField(primary_key=True, db_column='option_id')
	wname = models.CharField(max_length=64, unique=True,db_column='option_name')
	wvalue = models.TextField(db_column='option_value')
	wautoload = models.CharField(max_length=20, default='yes',db_column='autoload')

	class Meta:
		db_table = 'wp_options'

	def __unicode__(self):
		return self.wname

class Wuser(models.Model):
	wid = models.AutoField(primary_key=True, db_column='ID')
	wusername = models.CharField(max_length=60, db_column='user_login')
	wpassword = models.CharField(max_length=64, db_column='user_pass')
	wnickname = models.CharField(max_length=50, db_column='user_nicename')
	wemail = models.EmailField(max_length=100, db_column='user_email')
	wuserurl = models.CharField(max_length=100, db_column='user_url')
	wregisteredtime = models.DateTimeField(default=datetime.now(), db_column='user_registered')
	wactivationkey = models.CharField(max_length=60, db_column='user_activation_key')
	wstatus = models.IntegerField(default=0, db_column='user_status')
	wdisplayname = models.CharField(max_length=255, db_column='display_name')

	class Meta:
		db_table = 'wp_users'

	def __unicode__(self):
		return self.wusername

class Wusermeta(models.Model):
	wid = models.AutoField(primary_key=True, db_column='umeta_id')
	wuser = models.ForeignKey(Wuser, db_column='user_id')
	wmetakey = models.CharField(max_length=255, db_column='meta_key')
	wmetavalue = models.TextField(default='', db_column='meta_value')

	class Meta:
		db_table = 'wp_usermeta'

	def __unicode__(self):
		return self.wmetakey

class Wterm(models.Model):
	wid = models.AutoField(primary_key=True, db_column='term_id')
	wname = models.CharField(max_length=200, db_column='name')
	wslug = models.CharField(max_length=200, unique=True, db_column='slug')
	wtermgroup = models.BigIntegerField(default=0, db_column='term_group')

	class Meta:
		db_table = 'wp_terms'

	def __unicode__(self):
		return self.wname

class Wtermtaxonomy(models.Model):
	wid = models.AutoField(primary_key=True, db_column='term_taxonomy_id')
	wterm = models.ForeignKey(Wterm, db_column='term_id')
	wtaxonomy = models.CharField(max_length=32, db_column='taxonomy')
	wdescription = models.TextField(db_column='description')
	wparent = models.BigIntegerField(default=0, db_column='parent')
	wcount = models.BigIntegerField(default=0, db_column='count')

	class Meta:
		db_table = 'wp_term_taxonomy'

	def __unicode__(self):
		return self.wtaxonomy

class Wtermrelationship(models.Model):
	wid = models.AutoField(primary_key=True, db_column='object_id')
	wtermtaxonomy = models.ForeignKey(Wtermtaxonomy, db_column='term_taxonomy_id')
	wtermorder = models.IntegerField(default=0, db_column='term_order')

	class Meta:
		db_table = 'wp_term_relationships'

	def __unicode__(self):
		return self.wtermorder


POST_STATUS_CHOICES = (
						('publish', u'已发布'),
						('wait', u'等待复审'),
						('draft', u'草稿'),
						)

class Wpost(models.Model):
	wid = models.AutoField(primary_key=True, db_column='ID')
	wauthor = models.ForeignKey(Wuser, related_name='+', db_column='post_author')
	wpostdate = models.DateTimeField(default=datetime.now(), db_column='post_date')
	wpostdategmt = models.DateTimeField(default=datetime.now(), db_column='post_date_gmt')
	wcontent = models.TextField(db_column='post_content')
	wtitle = models.CharField(max_length=300, verbose_name=u'文章标题', db_column='post_title')
	wexcerpt = models.TextField(db_column='post_excerpt')
	wstatus = models.CharField(max_length=20, choices=POST_STATUS_CHOICES, default='publish', db_column='post_status')
	wcommentstatus = models.CharField(max_length=20, default='open', db_column='comment_status')
	wpingstatus = models.CharField(max_length=20, default='open', db_column='ping_status')
	wpostpassword = models.CharField(max_length=20, db_column='post_password')
	wpostname = models.CharField(max_length=200, db_column='post_name')
	wtoping = models.TextField(db_column='to_ping')
	wpinged = models.TextField(db_column='pinged')
	wpostmodified = models.DateTimeField(default=datetime.now(), db_column='post_modified')
	wpostmodifiedgmt = models.DateTimeField(default=datetime.now(), db_column='post_modified_gmt')
	wcontentfiltered = models.TextField(db_column='post_content_filtered')
	wpostparent = models.BigIntegerField(default=0, db_column='post_parent')
	wguid = models.CharField(max_length=255, db_column='guid')
	wmenuorder = models.IntegerField(default=0, db_column='menu_order')
	wposttype = models.CharField(max_length=20, default='post', db_column='post_type')
	wpostmimetype = models.CharField(max_length=100, db_column='post_mime_type')
	wcommentcount = models.BigIntegerField(default=0, db_column='comment_count')


	class Meta:
		db_table = 'wp_posts'
		verbose_name = verbose_name_plural = u'日志'

	def __unicode__(self):
		return self.wtitle

class Wpostmeta(models.Model):
	wid = models.AutoField(primary_key=True, db_column='meta_id')
	wpost = models.ForeignKey(Wpost, db_column='post_id')
	wmetakey = models.CharField(max_length=255, db_column='meta_key')
	wmetavalue = models.TextField(db_column='meta_value')

	class Meta:
		db_table = 'wp_postmeta'

	def __unicode__(self):
		return self.wmetakey

class Wcomment(models.Model):
	wid = models.AutoField(primary_key=True, db_column='comment_ID')
	wpost = models.ForeignKey(Wpost, default=0, db_column='comment_post_ID')
	wcommentauthor = models.TextField(db_column='comment_author')
	wcommentauthoremail = models.EmailField(max_length=100, db_column='comment_author_email')
	wcommentauthorurl = models.CharField(max_length=200, db_column='comment_author_url')
	wcommentauthorip = models.CharField(max_length=100, db_column='comment_author_IP')
	wcommenttime = models.DateTimeField(default=datetime.now(), db_column='comment_date')
	wcommenttimegmt = models.DateTimeField(default=datetime.now(), db_column='comment_date_gmt')
	wcommentcontent = models.TextField(db_column='comment_content')
	wcommentkarma = models.IntegerField(default=0, db_column='comment_karma')
	wcommentapproved = models.CharField(max_length=20, default='', db_column='comment_approved')
	wcommentagent = models.CharField(max_length=255, db_column='comment_agent')
	wcommenttype = models.CharField(max_length=20, db_column='comment_type')
	wcommentparent = models.ForeignKey('self', default=0, db_column='comment_parent')
	wuser = models.ForeignKey(Wuser, default=0, db_column='user_id')

	class Meta:
		db_table = 'wp_comments'


	def __unicode__(self):
		return self.wcommentauthor

class Wcommentmeta(models.Model):
	wid = models.AutoField(primary_key=True, db_column='meta_id')
	wcomment = models.ForeignKey(Wcomment, default=0, db_column='comment_id')
	wmetakey = models.CharField(max_length=255, db_column='meta_key')
	wmetavalue = models.TextField(db_column='meta_value')

	class Meta:
		db_table = 'wp_commentmeta'

	def __unicode__(self):
		return self.wmetakey





























	