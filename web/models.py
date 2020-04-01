from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class logo(models.Model):
    obrazek = models.ImageField(upload_to='images',
                                height_field=None,
                                width_field=None,
                                max_length=None, )

    def save(self, *args, **kwargs):
        if not self.pk and logo.objects.exists():
            raise ValidationError('Může být jenom jedno Logo')
        return super(logo, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Logo'

    def __str__(self):
        return "Logo"


class produkt(models.Model):
    Nazev = models.CharField(max_length=30)
    cena = models.CharField(max_length=30)
    obrazek = models.ImageField(upload_to='images',
                                height_field=None,
                                width_field=None,
                                max_length=None, )

    kategorie = models.CharField(choices=[("HRNKY", "HRNKY"),
                                          ("MÍSY A TÁCI", "MÍSY A TÁCI"),
                                          ("KONVIČKY", "KONVIČKY"),
                                          ("MISKY", "MISKY"),
                                          ("VÁZY", "VÁZY"),
                                          ("DŽBÁNY A KORBELY", "DŽBÁNY A KORBELY"),
                                          ], default="HRNKY", max_length=20)
    cas = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Produkty'

    def __str__(self):
        return self.Nazev


class Kontakt(models.Model):
    majitel = models.CharField(max_length=30, default=" ")
    bydliste = models.CharField(max_length=30)
    telefoniCislo = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    instagram = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        if not self.pk and Kontakt.objects.exists():
            raise ValidationError('Může být jenom jeden Kontakt')
        return super(Kontakt, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Kontakt'

    def __str__(self):
        return "Moje Kontakty"


class Autor(models.Model):
    informace = models.TextField()

    def save(self, *args, **kwargs):
        if not self.pk and Autor.objects.exists():
            raise ValidationError('Může být jenom jeden Autor')
        return super(Autor, self).save(*args, **kwargs)

    class Autor:
        verbose_name_plural = 'Autor'

    def __str__(self):
        return "Autor - Informace"


