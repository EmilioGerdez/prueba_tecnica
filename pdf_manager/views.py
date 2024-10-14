from django.shortcuts import render
import pymupdf
from .models import FutaModel
# Create your views here.


def Fill_Futa(pk:int):
    futa = FutaModel.objects.get(pk=pk)
    futaValuesList = [
        futa.EiNumber[:2],
        futa.EiNumber[2:],
        futa.LegalName,
        futa.ComercialName,
        futa.Address,
        futa.City,
        futa.State,
        futa.Zip
    ]
    doc = pymupdf.open("file.pdf") #load file
    counter =0
    for page in doc:
        for field in page.widgets():
            field.field_value= counter
            field.update()
            counter+=1