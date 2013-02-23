#coding=utf-8
from django.contrib import admin
from myblog.models import *

class UserAdmin(admin.ModelAdmin):
	list_display = ('name', 'Email', 'gender', 'avatar')
	search_field = ('name')

class BlogAdmin(admin.ModelAdmin):
	list_display = ('caption', 'author', 'publish_time')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
	list_display = ('tag_name',)

admin.site.register(User, UserAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)

