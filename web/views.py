from django.template import loader
from .models import logo, produkt, Kontakt, Autor
from django.http import HttpResponse


def nejnovejsiprodukty(request):



    context = {"Title": "NEJNOVĚJŠÍ PRODUKTY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": produkt.objects.order_by('-cas')[:15]
               }
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def hrnky(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie== "HRNKY":
            allKategorii.append(element)

    context = {"Title": "HRNKY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii
               }
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def misyATaci(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie == "MÍSY A TÁCI":
            allKategorii.append(element)

    context = {"Title": "MÍSY A TÁCI",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii}
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def konvicky(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie == "KONVIČKY":
            allKategorii.append(element)
    context = {"Title": "KONVIČKY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii}
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def misky(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie == "MISKY":
            allKategorii.append(element)
    context = {"Title": "MISKY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii
               }
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def vazy(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie == "VÁZY":
            allKategorii.append(element)
    context = {"Title": "VÁZY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii
               }
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def dzbanyAKorbele(request):
    allKategorii = []
    for element in produkt.objects.all():
        if element.kategorie == "DŽBÁNY A KORBELY":
            allKategorii.append(element)
    context = {"Title": "DŽBÁNY A KORBELY",
               "Logo": logo.objects.get(pk=1).obrazek.name,
               "ProduktList": allKategorii
               }
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def keramika(request):
    context = {}
    template = loader.get_template('Home.html')
    return HttpResponse(template.render(context, request))


def About(request):
    context = {"Logo": logo.objects.get(pk=1).obrazek.name,
               "Title": "",
               "Informace": Autor.objects.get(pk=1).informace}
    template = loader.get_template('Autor.html')
    return HttpResponse(template.render(context, request))


def Contact(request):
    context = {"Logo": logo.objects.get(pk=1).obrazek.name,
               "Kontakt": Kontakt.objects.get(pk=1),
               "Title": ""}
    template = loader.get_template('Kontakt.html')
    return HttpResponse(template.render(context, request))
