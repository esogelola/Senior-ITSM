from django.contrib import admin
from .models import Hardware, Contract, Software





# Register your models here.
@admin.register(Hardware)
class HardwareAdmin(admin.ModelAdmin):
    list_display = ('hostname',)
    
    def get_queryset(self, request):
        # modify the queryset to clear ordering and limit to 1000
        qs = super(HardwareAdmin, self).get_queryset(request).order_by()

        return qs
        

       





    


admin.site.register(Contract)
admin.site.register(Software)