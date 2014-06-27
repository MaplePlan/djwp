from django.contrib import admin

# Register your models here.

from base.models import *

admin.site.register(Wlink)
admin.site.register(Woption)
admin.site.register(Wuser)
admin.site.register(Wusermeta)
admin.site.register(Wpost)
admin.site.register(Wpostmeta)
admin.site.register(Wcomment)
admin.site.register(Wcommentmeta)
admin.site.register(Wterm)
admin.site.register(Wtermtaxonomy)
admin.site.register(Wtermrelationship)