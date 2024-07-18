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


        

class Men(models.Model):
    st = models.ForeignKey(Product,on_delete=models.CASCADE ,related_name='men_by_product_s_t')
    pt = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='men_by_product_p_t')
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
