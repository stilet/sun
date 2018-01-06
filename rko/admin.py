from django.contrib import admin
from .models import  Rko


class RkoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'created_date', 'month', 'year', 'summ_fond', 'comment')
    list_filter = ['month', 'year']
    date_hierarchy = 'created_date'


admin.site.register(Rko, RkoAdmin)
