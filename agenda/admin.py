from django.contrib import admin

from .models import Task, Category, Project, Comment, Attachment

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Attachment)
