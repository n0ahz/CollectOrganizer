from django.contrib import admin

from configs.models import LibraryPath
# Register your models here.


class PathsAdmin(admin.ModelAdmin):
    # extra modification of the admin page...
    list_display = ['media_type', 'media_path']


admin.site.register(LibraryPath, PathsAdmin)
