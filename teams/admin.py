from django.contrib import admin
from teams.models import *

class OrganizationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Athlete)
admin.site.register(Team)
admin.site.register(Season)
admin.site.register(League)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Game)
