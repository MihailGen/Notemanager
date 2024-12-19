# admin.py
from django.contrib import admin
from .models import Note

'''
class CommentInline(admin.TabularInline):
    model = Comment


class CategoryInline(admin.TabularInline):
    model = Category


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'due_date', 'category')
    search_fields = ('id', 'name', 'description', 'category')
    list_filter = ('id', 'due_date', 'author', 'category')

    inlines = [CommentInline, ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')
    search_fields = ('id', 'name', 'color')
    list_filter = ('id', 'name', 'color')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'text', 'created_at')
    search_fields = ('task', 'text', 'created_at')
    list_filter = ('task', 'text', 'created_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

'''

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at', 'user')
    search_fields = ('title', 'created_at', 'updated_at', 'user')
    list_filter = ('created_at', 'updated_at', 'user')
