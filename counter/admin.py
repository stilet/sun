from django.contrib import admin
from .models import CounterE


# Просмотр в админке с разбитием по столбцам
class CounterEAdmin(admin.ModelAdmin):
    list_display = ('autor', 'created_date', 'month', 'year', 'indication_day',
                    'indication_night', 'home')
    list_filter = ['month', 'year']
    date_hierarchy = 'created_date'


admin.site.register(CounterE, CounterEAdmin)

