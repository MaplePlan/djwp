import json
import sys
import platform

import django

from models import *
from constants import *

def make_json_response(data, code):
	"""
	Make json response
	"""
	return json.dumps({'data':data, 'code':code, 'msg':CODE_MAP[code]})

#########################
## Get Site Infomation ##
#########################
def get_site_title():
	return {'site_title':SITE_TITLE}

def get_site_sub_title():
	return {'site_sub_title':SITE_SUB_TITLE}

def get_site_url():
	return {'site_url': SITE_URL}

def get_site_description():
	return {'site_description': SITE_DESCRIPTION}

def get_site_language():
	return {'site_language': WPLANG}

def secret_key_generator():
	"""
	Generator secret key
	"""
	pass


#######################
## Get System Status ##
#######################

def get_os_status():
	data = {
		'os':platform.platform()
	}
	return data

def get_djwp_status():
	data = {
		'python':platform.python_version(),
		'django':django.get_version(),
	}
	return data




















