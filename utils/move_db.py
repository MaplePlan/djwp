#coding=utf-8

# Suit for WordPress 3.8.1

app_name = 'base'

db_map = {
	'wp_commentmeta':[
		'_'.join([app_name, 'wcommentmeta']),
		[
			('meta_id', 'id'), 
			('comment_id', 'wcomment_id'), 
			('meta_key', 'wmetakey'), 
			('meta_value', 'wmetavalue')
		]
	],
	'wp_comments':[
		'_'.join([app_name, 'wcomment']),
		[
			('comment_ID', 'id'), 
			('comment_post_ID', 'wpost_id'), 
			('comment_author', 'wcommentauthor'), 
			('comment_author_email', 'wcommentauthoremail'), 
			('comment_author_url', 'wcommentauthorurl'),
			('comment_author_IP', 'wcommentauthorip'), 
			('comment_date', 'wcommenttime'), 
			('comment_date_gmt', 'wcommenttimegmt'), 
			('comment_content', 'wcommentcontent'), 
			('comment_karma', 'wcommentkarma'),
			('comment_approved', 'wcommentapproved'), 
			('comment_agent', 'wcommentagent'), 
			('comment_type', 'wcommenttype'), 
			('comment_parent', 'wcommentparent'), 
			('user_id', 'wuser_id')
		]
	],
	'wp_links':[
		'_'.join([app_name, 'wlink']),
		[
			('link_id', 'id'), 
			('link_url', 'wurl'), 
			('link_name', 'wname'), 
			('link_image', 'wimage'), 
			('link_target', 'wtarget'), 
			('link_description', 'wdescription'), 
			('link_visible', 'wvisible'), 
			('link_owner', 'wowner'), 
			('link_rating', 'wrating'), 
			('link_updated', 'wupdated'), 
			('link_rel', 'wrel'),
			('link_notes', 'wnotes'),
			('link_rss', 'wrss')
		]
	],
	'wp_options':[
		'_'.join([app_name, 'woption']),
		[
			('option_id', 'id'), 
			('option_name', 'wname'), 
			('option_value', 'wvalue'), 
			('autoload', 'wautoload')
		]
	],
	'wp_postmeta':[
		'_'.join([app_name, 'wpostmeta']),
		[
			('meta_id', 'id'),
			('post_id', 'wpost_id'), 
			('meta_key', 'wmetakey'), 
			('meta_value', 'wmetavalue')
		]
	],
	'wp_posts':[
		'_'.join([app_name, 'wpost']),
		[
			('ID', 'id'), 
			('post_author', 'wauthor_id'), 
			('post_date', 'wpostdate'), 
			('post_date_gmt', 'wpostdategmt'), 
			('post_content', 'wcontent'), 
			('post_title', 'wtitle'),
			('post_excerpt', 'wexcerpt'), 
			('post_status', 'wstatus'), 
			('comment_status', 'wcommentstatus'), 
			('ping_status', 'wpingstatus'), 
			('post_password', 'wpostpassword'),
			('post_name', 'wpostname'), 
			('to_ping', 'wtoping'), 
			('pinged', 'wpinged'), 
			('post_modified', 'wpostmodified'), 
			('post_modified_gmt', 'wpostmodifiedgmt'),
			('post_content_filtered', 'wcontentfiltered'), 
			('post_parent', 'wpostparent_id'), 
			('guid', 'wguid'), 
			('menu_order', 'wmenuorder'), 
			('post_type', 'wposttype'),
			('post_mime_type', 'wpostmimetype'), 
			('comment_count', 'wcommentcount')
		]
	],
	'wp_terms':[
		'_'.join([app_name, 'wterm']),
		[
			('term_id', 'id'),
			('name', 'wname'),
			('slug', 'wslug'),
			('term_group', 'wtermgroup')
		]
	],
	'wp_term_relationships':[
		'_'.join([app_name, 'wtermrelationship']),
		[
			('object_id', 'id'),
			('term_taxonomy_id', 'wtermtaxonomy_id'),
			('term_order', 'wtermorder')
		]
	],
	'wp_term_taxonomy':[
		'_'.join([app_name, 'wtermtaxonomy']),
		[
			('term_taxonomy_id', 'id'),
			('term_id', 'wterm_id'),
			('taxonomy', 'wtaxonomy'),
			('description', 'wdescription'),
			('parent', 'wparent'),
			('count', 'wcount')
		]
	],
	'wp_users':[
		'_'.join([app_name, 'wuser']),
		[
			('ID', 'id'),
			('user_login', 'wusername'),
			('user_pass', 'wpassword'),
			('user_nicename', 'wnickname'),
			('user_email', 'wemail'),
			('user_url', 'wuserurl'),
			('user_registered', 'wregisteredtime'),
			('user_activation_key', 'wactivationkey'),
			('user_status', 'wstatus'),
			('display_name', 'wdisplayname')
		]
	],
	'wp_usermeta':[
		'_'.join([app_name, 'wusermeta']),
		[
			('umeta_id', 'id'),
			('user_id', 'wuser_id'),
			('meta_key', 'wmetakey'),
			('meta_value', 'wmetavalue')
		]
	],
}


if __name__ == '__main__':

	import csv

	import sys
	import os

	#import MySQLdb

	sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	import djwp.settings

	db_config = djwp.settings.DATABASES['default']

	wdb_dump_file = '/Users/maple/Desktop/wp_crazytech.sql'

	fobj = open(wdb_dump_file)
	lines = fobj.readlines()
	for i in xrange(len(lines)):
		if 'LOCK' in lines[i]:
			for k,v in db_map.items():
				if k in lines[i]:
					lines[i] = lines[i].replace(k, v[0])
					break
		if 'INSERT' in lines[i]:
			for k,v in db_map.items():
				if k in lines[i].split()[2]:
					lines[i] = lines[i].replace(k, v[0], 1)
					for k1, v1 in v[1]:
						if k1 in lines[i]:
							lines[i] = lines[i].replace(k1, v1)
		print lines[i]
	db_host = db_config.get('HOST', '127.0.0.1')
	db_name = db_config.get('NAME', '')
	db_user = db_config.get('USER', '')
	db_pswd = db_config.get('PASSWORD', '')

	#conn = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pswd, db=db_name, charset='utf8')
	#cursor = conn.cursor()

	for k,v in db_map.items():
		sql = ''
		wtable = k
		dtable = v[0]
		
	#cursor.close()
	#conn.close()


			

		