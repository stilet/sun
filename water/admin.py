from django.contrib import admin

from .models import CounterW


class CounterWAdmin(admin.ModelAdmin):
    list_display = ('autor', 'created_date', 'month', 'year', 'indication', 'home')
    list_filter = ['month', 'year']
    date_hierarchy = 'created_date'


admin.site.register(CounterW, CounterWAdmin)
