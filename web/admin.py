from django.contrib import admin

# Register your models here.
from .models import logo, produkt

admin.site.site_header = 'Keramika Koller - admin'


class ProduktAdmin(admin.ModelAdmin):
    exclude = ('cas',)


admin.site.register(logo)
admin.site.register(produkt, ProduktAdmin)
