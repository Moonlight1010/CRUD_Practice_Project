from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'user', 'complete')
    list_display_link = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)


