from django.shortcuts import render
import pymupdf
from .models import FutaModel
# Create your views here.


def Fill_Futa(pk:int):
    futa = FutaModel.objects.get(pk=pk)
    TotalEmployePaymentWhole,TotalEmployePaymentDecimal = futa.TotalEmployePayment.split(".") #verificar que sea un punto o una coma
    ExentPaymentWhole,ExentPaymentDecimal = futa.ExentPayment.split(".") #verificar que sea un punto o una coma
    futaValuesList = [
        futa.EiNumber[:2],
        futa.EiNumber[2:],
        futa.LegalName,
        futa.ComercialName,
        futa.Address,
        futa.City,
        futa.State,
        futa.Zip,
        futa.ForeignCountry,
        futa.ForeignState,
        futa.ForeignState,
        futa.DeclarationA,
        futa.DeclarationB,
        futa.DeclarationC,
        futa.DeclarationD,
        futa.Pt1A1,
        futa.Pt1A2,
        futa.Pt1B,
        futa.Pt12,
        TotalEmployePaymentWhole,
        TotalEmployePaymentDecimal,
        ExentPaymentWhole,
        ExentPaymentDecimal,
        futa.SupplementaryBenefits,
        futa.LifeInsurance,
        futa.Retire,
        futa.DependantsCare,
        futa.Other,
        



    ]
    doc = pymupdf.open("file.pdf") #load file
    counter =0
    for page in doc:
        for field in page.widgets():
            field.field_value= counter
            field.update()
            counter+=1