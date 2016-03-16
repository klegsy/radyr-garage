from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomerForm, EmployeeForm, InvoiceForm
from django.views.generic import DetailView



from system.models import Invoice, Parts


def options(request):
    return render(request, 'system/options.html', {})


def employee_new(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('system.views.employee_detail')
    else:
        form = EmployeeForm()
    return render(request, 'system/employee_edit.html', {'form': form})


def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('system.views.customer_detail')
    else:
        form = CustomerForm()
    return render(request, 'system/customer_edit.html', {'form': form})


'''class InvoiceView(DetailView):
    model = Invoice
    template_name = 'system/invoice_detail.html'''''


def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'system/invoice_detail.html', {'invoice': invoice})

def invoice_new(request):
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('system.views.invoice_new')
    else:
        form = InvoiceForm()
    return render(request, 'system/invoice_edit.html', {'form': form})
