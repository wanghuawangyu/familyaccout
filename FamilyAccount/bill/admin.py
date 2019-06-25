from django.contrib import admin
from .models import *
# Register your models here.

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['familyName','addDate']
    list_display_links=['familyName']
    # list_editable=['familyName']
    # list_filter=['addDate']
    search_fields=['familyName']
    date_hierarchy='addDate'

class UserAdmin(admin.ModelAdmin):
    list_display = ['userName','userTel','userEmail','haveFamily','isFamilyHead','isActive','addDate','family_id','familyMarkName','familyOrderNumber']
    list_display_links=['userName']
    list_editable=['userTel','userEmail','haveFamily','isFamilyHead','isActive','family_id','familyMarkName','familyOrderNumber']
    list_filter=['haveFamily','isFamilyHead','isActive','family_id']
    search_fields=['userName','userTel','userEmail']
    date_hierarchy='addDate'

class TradeAdmin(admin.ModelAdmin):
    list_display = ['tradeName','tradeDescrition','tradeOrderNumber','tradeOrderMark','tradeTypeToUser','addDate']
    list_display_links=['tradeName']
    list_editable=['tradeDescrition','tradeOrderNumber','tradeOrderMark','tradeTypeToUser']
    list_filter=['tradeTypeToUser']
    search_fields=['tradeName','tradeTypeToUser']
    date_hierarchy='addDate'

class CardAdmin(admin.ModelAdmin):
    list_display = ['cardName','cardDescrition','cardType','cardNumber','cardFixedCredits','cardStartAmount','cardBillday','cardRepaymentDay','isCardActive','isCardCount','cardOrderNumber','cardRemark','cardToUser','addDate']
    list_display_links=['cardName']
    list_editable=['cardDescrition','cardType','cardNumber','cardFixedCredits','cardStartAmount','cardBillday','cardRepaymentDay','isCardActive','isCardCount','cardOrderNumber','cardRemark','cardToUser']
    list_filter=['cardType','cardFixedCredits',]
    search_fields=['cardName','cardDescrition','cardNumber']
    date_hierarchy='addDate'

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subjectName','subjectDescrition','isSubjectActive','isSubjectCount','subjectOrderNumber','subjectToUser','addDate']
    list_display_links=['subjectName']
    list_editable=['subjectDescrition','isSubjectActive','isSubjectCount','subjectOrderNumber','subjectToUser']
    list_filter=['isSubjectActive','isSubjectCount','subjectToUser']
    search_fields=['subjectName','subjectDescrition','subjectToUser']
    date_hierarchy='addDate'

class DetailAdmin(admin.ModelAdmin):
    list_display = ['detailDate','tradeDate','tradeNumber','detailDescription','detailAmount','detailNo','installment','isCardOtherCredits','isDetailActive','detailToUser','detailToTradeType','detailToCard','detailToSubject']
    list_display_links=['tradeNumber']
    list_editable=['detailDescription','detailAmount','installment','isCardOtherCredits','isDetailActive','detailToUser','detailToTradeType','detailToCard','detailToSubject']
    list_filter=['installment','isCardOtherCredits','isDetailActive','detailToUser','detailToTradeType','detailToCard','detailToSubject']
    search_fields=['tradeNumber','detailDescription']
    date_hierarchy='tradeDate'

class BillAdmin(admin.ModelAdmin):
    list_display = ['addDate','billDate','billAmount','billRepaymentDate','isRepayment','billToUser','billToCard']
    list_display_links=['addDate']
    list_editable=['billDate','billAmount','billRepaymentDate','isRepayment','billToUser','billToCard']
    list_filter=['isRepayment','billToUser','billToCard']
    search_fields=['billToUser','billToCard']
    date_hierarchy='billRepaymentDate'

class InstallmentAdmin(admin.ModelAdmin):
    list_display = ["addDate",'installmentNumber','installmentDescription','installmentDate','installmentStartDate','installmentEndDate','installmentMonthNumner','isAllowPrepayment','prepaymentRate','repaymentMethod','interestRatePerYear','installmentAmount','isPayNextInterest','installmentToUser','InstallmentToCard']
    list_display_links=['installmentNumber']
    list_editable=['installmentDescription','installmentDate','installmentStartDate','installmentEndDate','installmentMonthNumner','isAllowPrepayment','prepaymentRate','repaymentMethod','interestRatePerYear','installmentAmount','isPayNextInterest','installmentToUser','InstallmentToCard']
    list_filter=['isAllowPrepayment','installmentToUser','InstallmentToCard']
    search_fields=['installmentNumber','installmentDescription','installmentToUser','InstallmentToCard']
    date_hierarchy='addDate'

admin.site.register(Family,FamilyAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Trade,TradeAdmin)
admin.site.register(Card,CardAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Detail,DetailAdmin)
admin.site.register(Bill,BillAdmin)
admin.site.register(Installment,InstallmentAdmin)
