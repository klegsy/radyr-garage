from django.contrib import admin
from django import forms
from .models import Customer, Vehicle, Employee, Invoice, Parts
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'telephone', 'house_num', 'street_name', 'city', 'postcode')

    def clean_telephone(self):
        data = self.cleaned_data['telephone']
        if len(data) != 11:
            raise forms.ValidationError("The telephone number must be 11 numbers")

        return data

    '''def clean(self):
        cleaned_data = super(CustomerForm, self).clean()
        first = cleaned_data.get("first_name")
        last = cleaned_data.get("last_name")

        if not first.isalpha() and last.isalpha():
            raise forms.ValidationError("Names must be letters only")'''


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerForm
    list_display = ('first_name', 'last_name', 'email', 'telephone')
    search_fields = ['^first_name', '^last_name']

admin.site.register(Customer, CustomerAdmin)

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehicle
        fields = ('customer', 'registration', 'manufacture', 'model', 'MOT_date', 'service_date', 'mileage',)

    def clean_manufacture(self):
        manufacture = self.cleaned_data['manufacture']

        if not manufacture.isalpha():
            raise forms.ValidationError("Manufacture must be letters only")

        return manufacture

class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm
    list_filter = ('MOT_date',)
    list_display = ('customer','registration', 'manufacture', 'model', 'MOT_date', 'mileage', )
    search_fields = ['registration', 'manufacture' ]
    actions = ['mail_view']
    list_select_related = True

    def mail_view(self, request, pk):
        obj = get_object_or_404(Vehicle, pk=pk)
        send_mail('MOT Reminder','Your MOT is due',
                  'robert@klentzeris.uk', [obj.customer.email],)
        self.message_user(request, 'MOT reminders successfully sent')
        return redirect(reverse('admin:system_vehicle_changelist'))
    mail_view.short_description = 'Send MOT reminder email'
    mail_view.allow_tags = True


admin.site.register(Vehicle, VehicleAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee', 'first_name', 'last_name', 'email', 'telephone')
    search_fields = ['^first_name', '^last_name']

admin.site.register(Employee, EmployeeAdmin)


class InvoiceAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('customer', 'issue_date', 'due_date', 'total_price')
    search_fields = ['customer__first_name', 'customer__last_name', 'parts__part_name']






admin.site.register(Invoice, InvoiceAdmin)


class PartsAdmin(admin.ModelAdmin):
    list_display = ('part_name', 'part_price')
    search_fields = ['part_name', 'part_price']

admin.site.register(Parts, PartsAdmin)


