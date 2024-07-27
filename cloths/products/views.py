from django.contrib.auth import login
from django.shortcuts import render, redirect 
from .forms import RegistrationForm
from .models import Product, Men, Women
from .serializers import ProductSerializer, MenSerializer, WomenSerializer
from django.views import generic
from .forms import MenForm, WomenForm
from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin  


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

class MenCreateView(LoginRequiredMixin, generic.CreateView):  
    model = Men  
    form_class = MenForm  
    template_name = 'men_form.html'  
    success_url = '/men/'  

class MenUpdateView(LoginRequiredMixin, generic.UpdateView):  
    model = Men  
    form_class = MenForm  
    template_name = 'men_form.html'  
    success_url = '/men/'  

class MenDeleteView(LoginRequiredMixin, generic.DeleteView):  
    model = Men  
    template_name = 'men_confirm_delete.html'  
    success_url = '/men/'
# views  for Women  
class WomenListView(generic.ListView):  
    model = Women  
    template_name = 'women_list.html'  

class WomenCreateView(LoginRequiredMixin, generic.CreateView):  
    model = Women  
    form_class = WomenForm  
    template_name = 'women_form.html'  
    success_url = '/women/'  

class WomenUpdateView(LoginRequiredMixin, generic.UpdateView):  
    model = Women  
    form_class = WomenForm  
    template_name = 'women_form.html'  
    success_url = '/women/'  

class WomenDeleteView(LoginRequiredMixin, generic.DeleteView):  
    model = Women  
    template_name = 'women_confirm_delete.html'  
    success_url = '/women/'
# registration view

def register(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            user = form.save()  
            login(request, user)  # Log in the user after registration  
            return redirect('men-list')  # Redirect to men list view after registration  
    else:  
        form = RegistrationForm()  
    return render(request, 'registration/register.html', {'form': form})






