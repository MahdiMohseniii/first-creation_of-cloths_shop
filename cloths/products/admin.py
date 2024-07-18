from django.contrib import admin
from .models import Product,Men

admin.site.register(Product)

class MenAdmin(admin.ModelAdmin):
    list_display = ('pt','st')
admin.site.register(Men)


