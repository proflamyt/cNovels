from django.contrib import admin


from novels.models import NovelModel, ChapterModel, MapType, Marker, Area

# Register your models here.

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'book')
    list_filter = ('book',)

admin.site.register(NovelModel)
admin.site.register(ChapterModel, ChapterAdmin)
admin.site.register(MapType)
admin.site.register(Marker)
admin.site.register(Area)