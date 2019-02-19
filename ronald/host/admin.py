from django.contrib import admin

# Register your models here.
from .models import Hospital, House, Guest

class Host(admin.ModelAdmin):
    # Only to create module
    pass

admin.site.register(Hospital, Host)
admin.site.register(House, Host)
admin.site.register(Guest, Host)