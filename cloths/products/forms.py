from django import forms
from .models import Men, Women


class MenForm(forms.ModelForm):
    class Meta:
        model = Men
        fields = ['Style_Type', 'Product_Type', 'price', 'size', 'image']

class WomenForm(forms.ModelForm):
    class Meta:
        model = Women
        fields = ['style_type', 'product_type', 'price', 'size', 'image']
