from django.contrib import admin  
from .models import Product, Men, Women  

class MenInlineAdmin(admin.TabularInline):  
    model = Men  
    fields = ('Style_Type', 'Product_Type', 'price', 'size', 'image')  
    fk_name = 'Style_Type'  # Specify FK to use  
    extra = 0

class WomenInlineAdmin(admin.TabularInline):  
    model = Women  
    fields = ('style_type', 'product_type', 'price', 'size', 'image')  
    fk_name = 'style_type'  # Specify FK to use  
    extra = 0


@admin.register(Product)  
class ProductAdmin(admin.ModelAdmin):  
    list_display = ('style', 'product_type', 'is_available')  
    inlines = (MenInlineAdmin, WomenInlineAdmin)



# admin.site.register(Women)

