from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin

from django.contrib.auth.admin import UserAdmin
from .models import Chapters,Maptype,NovelMap,MapPoint, Event, Genre, GroupChat, Message, Novel, Profile, Room, User, Weekly

admin.site.register(User)
admin.site.register(Weekly)
admin.site.register(Novel)
admin.site.register(Genre)
admin.site.register(Chapters)
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(GroupChat)
admin.site.register(Event)
admin.site.register(NovelMap)
admin.site.register(Maptype)
from leaflet.admin import LeafletGeoAdmin


class WeatherStationAdmin(LeafletGeoAdmin):
    settings_overrides = {
       'DEFAULT_CENTER': (6.0, 45.0),
       #'TILES': ['https://cartocdn-gusc.global.ssl.fastly.net/ramirocartodb/api/v1/map/named/tpl_756aec63_3adb_48b6_9d14_331c6cbc47cf/all/{z}/{x}/{y}.png']
       
    }
admin.site.register(MapPoint,WeatherStationAdmin)