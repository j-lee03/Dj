from django.contrib import admin

from bookmark.models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('nane', 'url' )
    list_filter_links = ('nane','url')
    search_filter = ('nane','url')


#admin.site.register(Bookmark,BookmarkAdmin)










