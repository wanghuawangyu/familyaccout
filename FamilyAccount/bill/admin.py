from django.contrib import admin
from .models import *
# Register your models here.

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['familyName','addDate']
    list_display_links=['familyName']


admin.site.register(Family,FamilyAdmin)
admin.site.register(User)
admin.site.register(Trade)
admin.site.register(Card)
admin.site.register(Subject)
admin.site.register(Detail)
admin.site.register(Bill)
admin.site.register(Installment)
