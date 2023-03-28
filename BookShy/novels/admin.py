from django.contrib import admin
from django.contrib.gis.admin import GeoModelAdmin


from novels.models import (NovelModel, ChapterModel, MapType, 
                           Marker, Area, UserBook, SnapShots, Genre)

# Register your models here.

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'book')
    list_filter = ('book',)


class CustomGeoAdmin(GeoModelAdmin):
    wms_url = 'http://127.0.0.1/novels/tiles/'

admin.site.register(NovelModel)
admin.site.register(ChapterModel, ChapterAdmin)
admin.site.register(MapType)
admin.site.register(Marker, CustomGeoAdmin)
admin.site.register(Area)
admin.site.register(UserBook)
admin.site.register(SnapShots)
admin.site.register(Genre)