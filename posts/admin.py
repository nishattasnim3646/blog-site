from django.contrib import admin
from posts.models import Post, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "publish_date"]
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
     list_display = ["id", "text"]

admin.site.register(Comment, CommentAdmin)