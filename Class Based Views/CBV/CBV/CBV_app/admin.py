from django.contrib import admin

# Register your models here.
from CBV.CBV_app.models import CBVViews


class CBVAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'description')
    list_filter = ('type', 'name')

admin.site.register(CBVViews)