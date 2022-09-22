from django.contrib import admin
from rentalspace.models import VansModel

class VansAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


admin.site.register(VansModel,VansAdmin)