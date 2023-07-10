from django.http import HttpResponse
from django.shortcuts import render
from ProDental.models import Odontologo

# Create your views here.
def odontologo(self):
    odontologo = Odontologo(nombre='Rezzo', direccion='Av. Pueyrredon 2431')
    odontologo.save()

    doc_texto = f'----> Odontologo: {odontologo.nombre} Direccion: {odontologo.direccion}'

    return HttpResponse(doc_texto)
