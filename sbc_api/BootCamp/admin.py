from django.contrib import admin
from BootCamp.models import BootCamp

class BootCampAdmin(admin.ModelAdmin):
    resource_class = BootCamp
    list_display = ['bootcamp_name', 'company_id', 'brand_name', 'program',
                    'tech_stack', 'price']
    search_fields = ['brand_name', 'bootcamp_name']

admin.site.register(BootCamp, BootCampAdmin)
