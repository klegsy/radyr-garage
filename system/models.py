from django.db import models
from decimal import Decimal
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.shortcuts import redirect



class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=11)
    house_num = models.CharField(max_length=3)
    street_name = models.CharField(max_length=35)
    city = models.CharField(max_length=20)
    postcode = models.CharField(max_length=9)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Vehicle(models.Model):
    customer = models.ForeignKey('Customer', null=True)
    registration = models.CharField(max_length=7)
    manufacture = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    MOT_date = models.DateField()
    service_date = models.DateField()
    mileage = models.PositiveIntegerField()

    def __str__(self):
        return self.registration


class Employee(models.Model):
    employee = models.ForeignKey('auth.User')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Parts(models.Model):
    part_name = models.CharField(max_length=15)
    part_price = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.part_name


class Invoice(models.Model):
    customer = models.ForeignKey('Customer')
    parts = models.ManyToManyField(Parts, related_name='parts')
    labour_time = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('0.00'))
    total_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    issue_date = models.DateField(null=True)
    due_date = models.DateField(null=True)

    def __str__(self):
        return str(self.customer) + " " + str(self.issue_date)




@receiver(m2m_changed, sender=Invoice.parts.through)
def calc_total(sender, instance, **kwargs):

    if instance.total_price == None:
        for parts in instance.parts.all():
            instance.total_price = (instance.labour_time*65)+(parts.part_price*parts.quantity)
            instance.save()
    else:
        pass