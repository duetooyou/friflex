from django.contrib import admin
from django.contrib.contenttypes.admin import GenericInlineModelAdmin
from .models import Content, Course, Rating, File, Text, Link


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'course')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
