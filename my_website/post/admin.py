from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'update', 'timestamp', 'content', 'size', 'money')
    list_filter = ('update', 'timestamp')
    list_editable = ('title', )
    list_display_links = ('update', )


admin.site.register(Post, PostAdmin)