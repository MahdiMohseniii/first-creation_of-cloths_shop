from django.db import models

class Product(models.Model):
    
    S_T = (
        ('classic','Classic'),
        ('modern','Modern'),
    )
    style = models.CharField(max_length=15,choices=S_T)

    P_T = (
        ('tshirt','T-Shirt'),
        ('shirt','Shirt'),
        ('pants','Pants'),
        ('skirt','Skirt'),
        ('dress','Dress'),
    )
    product_type = models.CharField(max_length=20, choices=P_T)
    is_available = models.BooleanField(default=True,blank=False)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_product_type_display()} ({'Available' if self.is_available else 'Not Available'})"
        

class Men(models.Model):
    Style_Type = models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='men_by_product_s_t')
    Product_Type = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='men_by_product_p_t')
    price = models.DecimalField(max_digits=15, decimal_places=2)

    size_type = (
        ('small','S'),
        ('medium','M'),
        ('large','L'),
        ('xlarge','XL'),
        ('xxlarge','XXL')
    )
    size = models.CharField(max_length=20, choices=size_type)
    image = models.ImageField(upload_to='product_images/')


class Women(models.Model):
    style_type = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Women_by_style_type')
    product_type = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Women_by_product_type')

    price = models.DecimalField(max_digits=15, decimal_places=2)

    size_type = (
        ('small','S'),
        ('medium','M'),
        ('large','L'),
        ('xlarge','XL'),
        ('xxlarge','XXL')
    )
    size = models.CharField(max_length=20, choices=size_type)
    image = models.ImageField(upload_to='product_images/')