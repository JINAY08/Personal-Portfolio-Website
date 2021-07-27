from django.contrib import admin
from . import models

# Register your models here.

class BookReviewAdmin(admin.ModelAdmin):
    list_display = ('title','description','author','image','link')
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
admin.site.register(models.BookReview,BookReviewAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','description','technology','image','link')
    list_filter = ('title',)
    ordering = ('title',)
    search_fields = ('title',)
admin.site.register(models.Project,ProjectAdmin)

