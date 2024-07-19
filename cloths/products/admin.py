from django.contrib import admin
from .models import Product,Men,Women


class ProductAdmin(admin.ModelAdmin):
    list_display = ('S_T','P_T','is_available')

admin.site.register(Product)

class MenAdmin(admin.ModelAdmin):
    list_display = ('pt','st')
admin.site.register(Men)


admin.site.register(Women)

