from django.contrib import admin

# Register your models here.
from .models import logo, produkt, Kontakt, Autor

admin.site.site_header = 'Keramika Koller - admin'


class ProduktAdmin(admin.ModelAdmin):
    exclude = ('cas',)


admin.site.register(produkt, ProduktAdmin)
admin.site.register(Kontakt)
admin.site.register(Autor)
admin.site.register(logo)
