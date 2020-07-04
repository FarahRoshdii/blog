from django.contrib import admin

from .models import Author, Genre, Post, Comment

admin.site.register(Author)
#admin.site.register(Post)
admin.site.register(Comment)


@admin.register(Post)
class GenreAdmin(admin.ModelAdmin):
    list_display =['title']
    list_filter = ['genre']

# admin.site.register(Genre)
