from django.contrib import admin
from .models import Content, Course, Rating, File, Text, Link


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pdf_file')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_type', 'course')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
