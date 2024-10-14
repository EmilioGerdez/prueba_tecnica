from operator import mod
from django.db import models
from django.utils import choices

# Create your models here.


class FutaModel(models.Model):

    EiNumber = models.CharField(max_length=9)
    LegalName = models.CharField(max_length=50)
    ComercialName = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Zip = models.CharField(max_length=5)
    ForeignCountry = models.CharField(max_length=50, null=True, blank=True)
    ForeignState = models.CharField(max_length=50, null=True, blank=True)
    ForeignZip = models.CharField(max_length=5, null=True, blank=True)
    DeclarationA = models.BooleanField()
    DeclarationB = models.BooleanField()
    DeclarationC = models.BooleanField()
    DeclarationD = models.BooleanField()
    Pt1A1 = models.CharField(max_length=1)
    Pt1A2 = models.CharField(max_length=1)
    Pt1B = models.BooleanField()
    Pt12 = models.BooleanField()
    TotalEmployePayment = models.CharField(max_length=50, null=True, blank=True)
    ExentPayment = models.CharField(max_length=50, null=True, blank=True)
    SupplementaryBenefits = models.BooleanField()
    LifeInsurance = models.BooleanField()
    Retire = models.BooleanField()
    DependantsCare = models.BooleanField()
    Other = models.BooleanField()
    ExcessPayment = models.CharField(max_length=50, null=True, blank=True)
    SubtotalPayment = models.CharField(max_length=50, null=True, blank=True)
    TotalSalary = models.CharField(max_length=50, null=True, blank=True)
    FutaFeePreAdjust = models.CharField(max_length=50, null=True, blank=True)
    FutaSalaryTotalFee = models.CharField(max_length=50, null=True, blank=True)
    SomesalaryFuta = models.CharField(max_length=50, null=True, blank=True)
    CreditReduction = models.CharField(max_length=50, null=True, blank=True)
    TotalFutaFeeAfterAdjust = models.CharField(max_length=50, null=True, blank=True)
    FutaFeeYearIncludingExcess = models.CharField(max_length=50, null=True, blank=True)
    BalanceDue =models.CharField(max_length=50, null=True, blank=True)
    ExcessPayment2 = models.CharField(max_length=50, null=True, blank=True)
    ApplyNextStatement = models.BooleanField()
    SendRefund = models.BooleanField()
    FirstTrimester = models.CharField(max_length=50, null=True, blank=True)
    SecondTrimester = models.CharField(max_length=50, null=True, blank=True)
    ThirdTrimester = models.CharField(max_length=50, null=True, blank=True)
    FourthTrimester = models.CharField(max_length=50, null=True, blank=True)
    TotalTaxLiability = models.CharField(max_length=50, null=True, blank=True)
    IRSEmployAllow = models.BooleanField()
    IRSPinNumber = models.CharField(max_length=5, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Position = models.CharField(max_length=50, null=True, blank=True)
    PhoneNumber = models.CharField(max_length=11, null=True, blank=True)
    SelfEmploy = models.BooleanField()
    PreparerName = models.CharField(max_length=50, null=True, blank=True)
    PreparerCompanyName = models.CharField(max_length=50, null=True, blank=True)
    PreparerAddress = models.CharField(max_length=50, null=True, blank=True)
    PreparerCity = models.CharField(max_length=50, null=True, blank=True)
    PreparerState = models.CharField(max_length=50, null=True, blank=True)
    PreparerZip = models.CharField(max_length=5, null=True, blank=True)
    PreparerPTIN =models.CharField(max_length=50, null=True, blank=True)
    PreparerEIN =models.CharField(max_length=50, null=True, blank=True)
    PreparerPhone =models.CharField(max_length=11, null=True, blank=True)
    PaymentAmountD = models.CharField(max_length=50, null=True, blank=True)
    PaymentAmountC = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.EiNumber)




