from django.contrib import admin
from blog.models import Blog
from blog.models import Todo

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Todo, BlogAdmin)
