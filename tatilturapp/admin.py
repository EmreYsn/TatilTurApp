from django.contrib import admin
from tatilturapp.models import TatilTur

# Register your models here.

class TatilTurAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username Group',{'fields':["username"]})
    ]

admin.site.register(TatilTur,TatilTurAdmin)