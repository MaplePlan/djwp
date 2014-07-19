from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import request
import json
import tenjin
from tenjin.helpers import *
# Create your views here.

from utils import *

###############
## API views ##
###############
def api_index(request):
	return HttpResponse(json.dumps({}))

def api_get_site_title(request):
	data, code = get_site_title(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_site_sub_title(request):
	data, code = get_site_sub_title(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_site_url(request):
	data, code = get_site_url(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_site_description(request):
	data, code = get_site_description(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_site_language(request):
	data, code = get_site_language(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_os_status(request):
	data, code = get_os_status(), '200'
	return HttpResponse(make_json_response(data, code))

def api_get_djwp_status(request):
	data, code = get_djwp_status(), '200'
	return HttpResponse(make_json_response(data, code))

################
## PAGE views ##
################

engine = tenjin.Engine(path=[os.path.join(os.path.dirname(__file__),'tpls')], postfix='.html', layout=':_layout')
global engine

def page_index(request):
	print request
	context = {
		'title': 'Tenjin Example',
		'items': ['AAA', 'BBB', 'CCC']
	}
	html = engine.render(':_layout', context)
	return HttpResponse(html)

