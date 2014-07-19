from django.contrib import admin

# Register your models here.

from base.models import *

admin.site.register(Wlink)
admin.site.register(Woption)
admin.site.register(Wuser)
admin.site.register(Wusermeta)

class WpostAdmin(admin.ModelAdmin):
	fields = ('wtitle','wcontent', 'wstatus')

admin.site.register(Wpost, WpostAdmin)
admin.site.register(Wpostmeta)
admin.site.register(Wcomment)
admin.site.register(Wcommentmeta)
admin.site.register(Wterm)
admin.site.register(Wtermtaxonomy)
admin.site.register(Wtermrelationship)