from django.contrib import admin
from locations.models import BjjLocation, BjjInstructor

# Register your models here.
class BjjLocationAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class BjjInstuctorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(BjjLocation, BjjLocationAdmin)
admin.site.register(BjjInstructor, BjjInstuctorAdmin)