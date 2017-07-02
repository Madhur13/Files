from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return self.name


from user_login.models import *        

class Offer(models.Model):
    company = models.ForeignKey(Company)
    description = models.CharField(max_length=1000)
    url = models.URLField()
    category = models.ForeignKey(Category)
    mailed = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)

    def __str__(self):
        return self.description

class Click(models.Model):
    user = models.ForeignKey(Customer)
    offer = models.ForeignKey(Offer)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True,editable=True)
    readonly_fields = ('created',)

    def __str__(self):
        return self.user.user.username+' '+self.offer.company.name

class Transaction(models.Model):
    user = models.ForeignKey(Customer)
    offer = models.ForeignKey(Offer)
    status = models.IntegerField()
    commission = models.FloatField(null=True,blank=True)
    cashback = models.FloatField(null=True,blank=True)
    referral = models.FloatField(null=True,blank=True)
    created = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    readonly_fields = ('created',)
    def __str__(self):
        return str(self.id)+' '+str(self.user.user)+' '+str(self.offer.company.name) 

    


    
