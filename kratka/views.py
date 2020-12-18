from django.http import HttpResponse
from django.shortcuts import render
from .models import Produkt

# Create your views here.

def home_widok(request, *args, **kwargs):
    queryset = Produkt.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "dom.html", context)

def produkt (request, id):
    produkt_user = Produkt.objects.get(pk=id)
    queryset = Produkt.objects.all()
    dane = {'produkt_user' : produkt_user, "object_list": queryset}
    return render(request, 'opis.html', dane)