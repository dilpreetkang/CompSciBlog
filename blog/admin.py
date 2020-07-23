from django.contrib import admin
from blog.models import Blog
from blog.models import Todo
from blog.models import About
class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Todo, BlogAdmin)
admin.site.register(About, BlogAdmin)
