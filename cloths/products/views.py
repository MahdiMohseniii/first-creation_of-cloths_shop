from .models import Product, Men, Women
from .serializers import ProductSerializer, MenSerializer, WomenSerializer
from django.views import generic
from .forms import MenForm, WomenForm
from rest_framework import generics

# these classes refers to API_VIEW
class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MenListCreate(generics.ListCreateAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer

class MenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Men.objects.all()
    serializer_class = MenSerializer


class WomenListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# these classes refers to Template_Views 

class MenListView(generic.ListView):  
    model = Men  
    template_name = 'men_list.html'  

class MenCreateView(generic.CreateView):  
    model = Men  
    form_class = MenForm  
    template_name = 'men_form.html'  
    success_url = '/men/'  

class MenUpdateView(generic.UpdateView):  
    model = Men  
    form_class = MenForm  
    template_name = 'men_form.html'  
    success_url = '/men/'  

class MenDeleteView(generic.DeleteView):  
    model = Men  
    template_name = 'men_confirm_delete.html'  
    success_url = '/men/'  

# views  for Women  
class WomenListView(generic.ListView):  
    model = Women  
    template_name = 'women_list.html'  

class WomenCreateView(generic.CreateView):  
    model = Women  
    form_class = WomenForm  
    template_name = 'women_form.html'  
    success_url = '/women/'  

class WomenUpdateView(generic.UpdateView):  
    model = Women  
    form_class = WomenForm  
    template_name = 'women_form.html'  
    success_url = '/women/'  

class WomenDeleteView(generic.DeleteView):  
    model = Women  
    template_name = 'women_confirm_delete.html'  
    success_url = '/women/'






