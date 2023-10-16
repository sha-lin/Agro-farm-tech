from django import forms
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
import datetime as dt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post,Business
from .form import BusinessForms,PostForms
from .form import ProductForm 



# farmer_app/views.py
from django.shortcuts import render, redirect
from .models import Product, ProductRequest
from django.contrib.auth.decorators import login_required

@login_required
class PostDetailView(DetailView):
    model=Post
    template_name='tfarmapp/dashboard.html'

def dashboard(request):
    products = Product.objects.filter(user=request.user)
    requests = ProductRequest.objects.filter(product__user=request.user)
    return render(request,'tfarmapp/dashboard.html',)
    return render(request, 'dashboard.html', {'products': products, 'requests': requests})

@login_required
# class PostDetailView(DetailView):
#     model=Post
#     template_name='tfarmapp/add_product.html'

def add_product(request):
    if request.method == 'POST':
     form = ProductForm(request.POST)
     if form.is_valid():
            # Create a new product object but don't save it to the database yet
            new_product = form.save(commit=False)
            
            # Assign the user to the product (assuming the user is logged in)
            new_product.user = request.user
            
            # Save the product to the database
            new_product.save()
            return redirect('dashboard')
    else:
        form = ProductForm()

    return render(request, 'tfarmapp/add_product.html', {'form': form})
        # Handle form submission and create a new product
        # You'll need to create a form for adding products

    return render(request, 'tfarmapp/add_product.html',)

@login_required
def view_requests(request):
    requests = ProductRequest.objects.filter(product__user=request.user)
    return render(request, 'tfarmapp/view_requests.html', {'requests': requests})


# Create your views here.
class BusinessListView(ListView):
    model = Business
    template_name= 'tfarmapp/home.html'
    context_object_name = 'businesses'
    
class BusinessDetailView(DetailView):
    model=Business
class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = Business
    fields=['name','email','business_image','location']
    template_name= 'tfarmapp/business_form.html'

    def form_valid(self,form):
        form.instance.business_owner = self.request.user
        return super().form_valid(form)

class BusinessUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model=Business
    fields = ['name','email','business_image','location']

    def form_valid(self):
        forms.instance.business_owner =self.request.user
        return super().form_valid()

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.business_owner:
            return True
        return False
    
class BusinessDeleteView(LoginRequiredMixin,DeleteView):
    model=Business
    success_url='/'
    template_name='tfarmapp/business_confirm_delete.html'
    
    def test_func(self):
        business=self.get_object()
        
        if self.request.user==business.business_owner:
            return True
        return False

class PostListView(ListView):
    model=Post
    template_name='tfarmapp/post_list.html'
    context_object_name='posts'
    ordering='-date_posted'

class PostCreateView(LoginRequiredMixin,CreateView,UserPassesTestMixin):
    model = Post
    fields = ['post']
    template_name='tfarmapp/post_form.html'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model=Post
    template_name='tfarmapp/post_confirm_delete.html'
    success_url='/'
    
    
    def test_func(self):
        post = self.get_object()
        
        if self.request.user ==post.author:
            return True
        return False
    
class PostDetailView(DetailView):
    model=Post
    template_name='tfarmapp/post_detail.html'

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    # template_name='tfarmapp/post_detail.html'
    fields = ['post']
    

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        
        return False
    

def search_request(request):
    if 'query' in request.POST and request.GET['query']: 
        search = request.GET.get('query')
        search_business= Business.search_by_title(search)
        messages= f'{search}'
        context = {"message":messages,"businesses":search_business}
        
        return render(request,'tfarmapp/search.html',context)

    else:
        message="You haven't searched for any item"
        return render(request,'tfarmapp/search.html',{"message":message}) 