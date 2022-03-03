from django.contrib import admin
from pacienti.models import Pacient


# Register your models here.

class PacientAdmin(admin.ModelAdmin):
    list_display = ['nume', 'telefon', 'email', 'gen', 'varsta', 'data_adaugarii']
    search_fields = ['nume', 'telefon', 'email', 'varsta']
    list_filter = ['gen']
    list_per_page = 10


admin.site.register(Pacient, PacientAdmin)
