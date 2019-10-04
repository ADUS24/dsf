from django.shortcuts import render
from .models import Product
from .forms import productForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def home(request):
    return render(request,'myapp/home.html')
def about(request):
    return render(request,'myapp/about.html')
@login_required
def contact(request):
    return render(request,'myapp/contact.html')
def productView(request):
    return render(request,'myapp/productView.html',{'products':None})

class updateProduct(UpdateView):
	model=Product
	fields=['name','price']
	success_url=reverse_lazy('myapp:productlist')
class productList(ListView):
	model=Product

class productDetails(DetailView):
	model=Product
class addProduct(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login')
	model=Product
	fields=['name','price']
	success_url=reverse_lazy('products')

class deleteProduct(DeleteView):
	model=Product
	success_url=reverse_lazy('myapp:productlist')