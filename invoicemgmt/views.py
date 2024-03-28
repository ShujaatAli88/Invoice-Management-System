from django.shortcuts import render, redirect
from . forms import InvoiceForm , InvoiceSearchForm ,UpdateInvoiceForm, RegistrationForm , LoginForm
from . models import Invoice , Registration
from django.http import HttpResponse
from django.contrib.auth import logout


def add_invoice(request):
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    recent_invices = Invoice.objects.order_by('-invoice_date')[:6]  #Recent 6 Invoices.....
    if form.is_valid():
        form.save()
        return redirect('add_invoice')
    
    context = {
        "recent_invoices" :recent_invices,
        "total_invoices" : total_invoices,
        "form":form,
        "title" : "New Invoice"
    }
    
    return render(request, 'entry.html',context)
    
def list_invoices(request):
    title = 'List of Invoices'
    query_Set = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    context = {
        "querySet" : query_Set,
        "title" : title,
        "form" : form
    }
    
    if request.method == "POST":
        query_Set = Invoice.objects.filter(invoice_number__icontains=form["invoice_number"].value())
        context = {
            "title" : title,
            "querySet":query_Set,
            "form" : form
        }
    
    return render(request, 'list_invoice.html',context)
    

def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)    
    form = UpdateInvoiceForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateInvoiceForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('list_invoices')
    context = {
        "form": form
    }
    
    return render(request, 'update.html', context)

def delete_invoice(request,pk):
    object = Invoice.objects.get(id=pk) 
    if request.method == "POST":
        object.delete() 
        return redirect('list_invoices')
    
    else:
        return render(request, 'delete_invoice.html')
    


def registration(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        print(form)
        form.save()
        # return redirect('login')
    
    context = {
        "form" : form
    }
    return render(request, 'home.html',context)


def dashboard(request):
    first_name = request.session.get("first_name",None)
    last_name = request.session.get("last_name",None)
    email = request.session.get("email",None)
    context = {
        "first_name" : first_name,
        "last_name" : last_name,
        "email" : email
    }
    return render(request, 'dashboard.html',context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("pass1")
            user = Registration.objects.filter(email=email, pass1=password).first()
            if user:
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                request.session['email'] = user.email
                return redirect('dashboard')
    
    return render(request, 'login.html')


def my_logout(request):
    logout(request)
    return render(request, 'logout.html')