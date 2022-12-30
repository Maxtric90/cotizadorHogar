from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CotizacionHogar
from .forms import CotizacionHogarForms
from .calculador import calculador

# Create your views here.
def hogar(request):
    desglosePremio = None
    if request.method== 'POST':
        form = CotizacionHogarForms(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            desglosePremio = calculador(cd)
    else:
        form = CotizacionHogarForms()
    return render(request, 'hogar/formulario.html',  {'form': form, 'desglosePremio': desglosePremio})

def hogarCotizado(request):
    desglosePremio = None
    if request.method== 'POST':
        form = CotizacionHogarForms(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            desglosePremio = calculador(cd)
    else:
        form = CotizacionHogarForms()
    return render(request, 'hogar/formularioCotizado.html',  {'form': form, 'desglosePremio': desglosePremio})
