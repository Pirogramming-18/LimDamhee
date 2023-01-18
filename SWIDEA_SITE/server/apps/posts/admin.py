from django.contrib import admin
from .models import Post, Devtool, IdeaStar
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Post)
admin.site.register(Devtool)
admin.site.register(IdeaStar)