from django.urls import path

from . import views

urlpatterns = [
    path('', views.nejnovejsiprodukty, name='nejnovejsiprodukty'),
    path('hrnky', views.hrnky, name='nejnovejsiprodukty'),
    path('misyATaci', views.misyATaci, name='nejnovejsiprodukty'),
    path('konvicky', views.konvicky, name='nejnovejsiprodukty'),
    path('misky', views.misky, name='nejnovejsiprodukty'),
    path('vazy', views.vazy, name='nejnovejsiprodukty'),
    path('dzbanyAKorbele', views.dzbanyAKorbele, name='nejnovejsiprodukty'),
    path('keramika', views.keramika, name='keramika'),
    path('oAutorovi', views.About, name='About'),
    path('kontakt', views.Contact, name='Kontakt'),

]
