from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('post', 'create_date',)
    search_fields = ('post', 'create_date')
    readonly_fields = ('create_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'post', 'create_date')
    search_fields = ('comment', 'create_date')
    readonly_fields = ('create_date',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
