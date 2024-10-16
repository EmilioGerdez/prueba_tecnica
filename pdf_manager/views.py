from django.http import HttpResponse
from django.shortcuts import render
import pymupdf
from .models import FutaModel
# Create your views here.


def Fill_Futa(request, pk:int):
    print("working")
    futa = FutaModel.objects.get(pk=pk)
    TotalEmployePaymentWhole,TotalEmployePaymentDecimal = futa.TotalEmployePayment.split(".") #verificar que sea un punto o una coma
    ExentPaymentWhole,ExentPaymentDecimal = futa.ExentPayment.split(".") #verificar que sea un punto o una coma
    ExcessPaymentWhole, ExcessPaymentDecimal = futa.ExcessPayment.split(".")
    SubtotalPaymentWhole,SubtotalPaymentDecimal = futa.SubtotalPayment.split(".")
    TotalSalaryWhole,TotalSalaryDecimal = futa.TotalSalary.split(".")
    FutaFeePreAdjustWhole, FutaFeePreAdjustDecimal= futa.FutaFeePreAdjust.split(".")
    FutaSalaryTotalFeeWhole, FutaSalaryTotalFeeDecimal = futa.FutaSalaryTotalFee.split(".")
    SomesalaryFutaWhole, SomesalaryFutaDecimal = futa.SomesalaryFuta.split(".")
    CreditReductionWhole, CreditReductionDecimal= futa.CreditReduction.split(".")
    TotalFutaFeeAfterAdjustWhole, TotalFutaFeeAfterAdjustDecimal = futa.TotalFutaFeeAfterAdjust.split(".")
    FutaFeeYearIncludingExcessWhole, FutaFeeYearIncludingExcessDecimal= futa.FutaFeeYearIncludingExcess.split(".")
    BalanceDueWhole, BalanceDueDecimal = futa.BalanceDue.split(".")
    ExcessPaymentWhole2, ExcessPaymentDecimal2 = futa.ExcessPayment2.split(".")
    FirstTrimesterWhole, FirstTrimesterDecimal = futa.FirstTrimester.split(".")
    SecondTrimesterWhole, SecondTrimesterDecimal = futa.SecondTrimester.split(".")
    ThirdTrimesterWhole, ThirdTrimesterDecimal = futa.ThirdTrimester.split(".")
    FourthTrimesterWhole, FourthTrimesterDecimal = futa.FourthTrimester.split(".")
    TotalTaxLiabilityWhole, TotalTaxLiabilityDecimal = futa.TotalTaxLiability.split(".")
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
        ExcessPaymentWhole,
        ExcessPaymentDecimal,
        SubtotalPaymentWhole,
        SubtotalPaymentDecimal,
        TotalSalaryWhole,
        TotalSalaryDecimal,
        FutaFeePreAdjustWhole,
        FutaFeePreAdjustDecimal,
        FutaSalaryTotalFeeWhole,
        FutaSalaryTotalFeeDecimal, 
        SomesalaryFutaWhole,
        SomesalaryFutaDecimal,
        CreditReductionWhole,
        CreditReductionDecimal,
        TotalFutaFeeAfterAdjustWhole,
        TotalFutaFeeAfterAdjustDecimal,
        FutaFeeYearIncludingExcessWhole,
        FutaFeeYearIncludingExcessDecimal,
        BalanceDueWhole,
        BalanceDueDecimal,
        ExcessPaymentWhole2,
        ExcessPaymentDecimal2,
        futa.ApplyNextStatement,
        futa.SendRefund,
        futa.LegalName,
        futa.EiNumber[:2],
        futa.EiNumber[2:],
        FirstTrimesterWhole,
        FirstTrimesterDecimal,
        SecondTrimesterWhole,
        SecondTrimesterDecimal,
        ThirdTrimesterWhole,
        ThirdTrimesterDecimal,
        FourthTrimesterWhole,
        FourthTrimesterDecimal,
        TotalTaxLiabilityWhole,
        TotalTaxLiabilityDecimal,
        futa.IRSEmployAllow,
        futa.IRSEmployName,
        futa.IRSEmployPhone,
        futa.IRSPinNumber[0], 
        futa.IRSPinNumber[1], 
        futa.IRSPinNumber[2], 
        futa.IRSPinNumber[3], 
        futa.IRSPinNumber[4], 
        not futa.IRSEmployAllow,
        futa.Name,
        futa.Position,
        futa.PhoneNumber,
        futa.SelfEmploy,
        futa.PreparerName,
        futa.PreparerPTIN,
        futa.PreparerCompanyName,
        futa.PreparerEIN,
        futa.PreparerAddress,
        futa.PreparerPhone,
        futa.PreparerCity,
        futa.PreparerState,
        futa.PreparerZip,
        futa.EiNumber[:2],
        futa.EiNumber[2:],
        futa.PaymentAmountD,
        futa.PaymentAmountC,
        futa.LegalName,
        futa.Address,
        futa.City + ", " + futa.State+ ", " + futa.Zip,
    ]
    doc = pymupdf.open("files/file.pdf") #load file
    counter =0
    for page in doc:
        for field in page.widgets():
            if futaValuesList[counter] is None:
                futaValuesList[counter]= ""
            if field.field_type ==2:
                if futaValuesList[counter]:
                    field.field_value = field.on_state()
            else:
                field.field_value= str(futaValuesList[counter])
            field.update()
            counter+=1
    doc.save("files/file"+str(pk)+".pdf")
    #return file
    with open("files/file"+str(pk)+".pdf", 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="files/file'+str(pk)+'.pdf"'
        return response
