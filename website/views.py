from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in.')
            return render(request,'home.html',{'records':records})
        else:
            messages.success(request,'username or password in wrong try again!')
            return redirect('home')
    else:
        print(records)
        return render(request,'home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out!')
    return redirect('home')
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print("form called")
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password = password)
            login(request,user)
            messages.success(request,"successfully you have been registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html', {"form":form})
    return render(request, 'register.html', {'form':form})
def customer_record(request,p):
    if request.user.is_authenticated:
        customer = Record.objects.get(id=p)
        return render(request, 'record.html', {'customer_record':customer})
    else:
        messages.success(request,"authentication failed")
        return redirect('home')
def delete_record(request,id):
    value= Record.objects.get(id=id)
    value.delete()
    messages.success(request,'Deleted record')
    return redirect('home')
def add_record(request):
    form=AddRecordForm(request.POST or None)
    #print(form)
    if request.user.is_authenticated:
        #print('hello')
        if request.method == 'POST':
            form = AddRecordForm(request.POST, request.FILES)
            
            #print(request.FILES)
            if form.is_valid():
                add_record = form.save()
                messages.success(request,'record added succesfully')
                return redirect('home')
            else:
                print(form.errors)
                messages.success(request,'form is not valid')
                return redirect('add_record')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,'you must be logged in')
        return redirect('home')
def update_record(request,id):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=id)
        form= AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'updated record')
            return redirect('home')
        return render(request,'update.html',{'form':form})
def view_vlog(request, id):
    if request.user.is_authenticated:
        vlog_record = Record.objects.get(id=id)
        
        return render(request, 'vlog.html', {'vlog_record': vlog_record})
    else:
        messages.success(request, "Authentication failed")
        return redirect('home')
