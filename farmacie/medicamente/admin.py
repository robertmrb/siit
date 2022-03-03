from django.contrib import admin
from medicamente.models import Medicament
# Register your models here.

class MedicamentAdmin(admin.ModelAdmin):
    list_display = ['numemedicament', 'stoc', 'unitate', 'data_expirarii']
    search_fields = ['numemedicament', 'stoc']
    list_filter = ['unitate']
    list_per_page = 10

admin.site.register(Medicament, MedicamentAdmin)