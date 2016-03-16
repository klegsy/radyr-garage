from django import forms
from .models import Employee, Customer, Vehicle, Invoice


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'telephone',)

    def clean_telephone(self):
        data = self.cleaned_data['telephone']
        if len(data) != 11:
            raise forms.ValidationError("The telephone number must be 11 numbers")

        return data


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'telephone',)

    def clean_telephone(self):
        data = self.cleaned_data['telephone']
        if len(data) != 11:
            raise forms.ValidationError("The telephone number must be 11 numbers")

        return data


class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('registration', 'manufacture', 'model', 'MOT_date', 'service_date', 'mileage',)

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('customer', 'parts', 'labour_time', 'total_price', 'issue_date', 'due_date')