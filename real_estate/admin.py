from django.contrib import admin

# Register your models here.
from real_estate.models import Location, House, HouseImage

admin.site.register(Location)


class HouseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'address_line_1', "city", "state", "market"]
    readonly_fields = ['slug', 'name']


admin.site.register(House, HouseModelAdmin)

admin.site.register(HouseImage)
