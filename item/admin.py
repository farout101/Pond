from django.contrib import admin

from .models import category, item

admin.site.register(category)
admin.site.register(item)