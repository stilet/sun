from django.contrib import admin
from .models import Homes


class HomesAdmin(admin.ModelAdmin):
    list_display = ('street', 'numhome', 'section', 'comment', 'owner')


admin.site.register(Homes, HomesAdmin)
