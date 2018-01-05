from django.contrib import admin
from .models import Pko


class RkoAdmin(admin.ModelAdmin):
    list_display = ('autor', 'created_date', 'month', 'year', 'summ_e',
                    'summ_w', 'summ_fond')
    list_filter = ['month', 'year']
    date_hierarchy = 'created_date'


admin.site.register(Pko, RkoAdmin)
