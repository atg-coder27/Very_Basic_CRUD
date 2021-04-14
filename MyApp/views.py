from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.http import HttpResponseRedirect
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    
    return render(request,'login.html',{'form':form})

def home_view(request):
    return render(request,'home.html')

def display_view(request):
    items = User.objects.all()
    print(items)
    return render(request,'display.html',{'items':items})

def edit_view(request,pk):
    item = User.objects.get(pk = pk)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            item.username = username
            item.email = email 
            item.password = password 
            item.save()
            return HttpResponseRedirect('/display')
    else:
        form = UserForm(initial={'username': item.username,'email':item.email,'password':item.password})
    
    return render(request,'edit.html',{'form':form})

def delete_view(request,pk):
    item = User.objects.get(pk = pk)
    item.delete()
    return HttpResponseRedirect('/display')

