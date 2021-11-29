from django.contrib import admin

# Register your models here.
from criminals.models import crime,criminal,documents,webimage,webvideo
admin.site.register(crime)
admin.site.register(criminal)
admin.site.register(documents)
admin.site.register(webimage)
admin.site.register(webvideo)