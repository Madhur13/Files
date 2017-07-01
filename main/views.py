from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import *
from user_login.models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from cashback.tasks import SendOfferEmail



def index(request):
    categories = Category.objects.all()
    offers = Offer.objects.all()
    template = loader.get_template('main/offers.html')
    results = template.render({'offers':offers}, request)
    return render(request, 'main/index.html', {'categories': categories, 'results':results})

def offers(request):
    company_ids = request.POST.getlist('comp_filter[]')
    category_ids = request.POST.getlist('cat_filter[]')
    if len(company_ids)==0 and len(category_ids)>=1:
        offers = Offer.objects.filter(category__id__in=category_ids)
    elif len(company_ids)==1 and len(category_ids)==0:
        offers = Offer.objects.filter(company__id__in=company_ids)
    else:
        offers = Offer.objects.filter(company__id__in=company_ids).filter(category__id__in=category_ids)
    if request.user.is_superuser:
        return render(request, 'main/emailoffersform.html', {'offers':offers})
    else:
        return render(request, 'main/offers.html', {'offers': offers})
    

def company(request,comp_name):
    categories = Category.objects.all()
    offers = Offer.objects.filter(company__name__iexact=comp_name)
    template = loader.get_template('main/offers.html')
    results = template.render({'offers':offers}, request)
    comp_id = get_object_or_404(Company, name__iexact=comp_name).id
    return render(request,'main/offer_page.html', {'categories':categories, 'results':results, 'comp_id': comp_id})

def category(request, cat_name):
    companies = Company.objects.all()
    offers = Offer.objects.filter(category__name__iexact=cat_name)
    template = loader.get_template('main/offers.html')
    results = template.render({'offers':offers}, request)
    cat_id = get_object_or_404(Category, name__iexact=cat_name).id
    return render(request, 'main/offer_page.html', {'companies':companies, 'results':results, 'cat_id': cat_id})

@login_required
def shop(request, offer_id):
    offer = Offer.objects.get(id=offer_id)
    customer = request.user.customer;
    click = Click(user=customer, offer=offer)
    click.save()
    link = offer.url;
    return HttpResponseRedirect('https://linksredirect.com/?pub_id=16923CL15205&subid='+str(click.id)+'&source=linkkit&url='+link)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def mailoffers(request):
    if(request.method=='POST'):
        offer_ids = request.POST.getlist('selected_offers[]')
        offers = Offer.objects.filter(id__in=offer_ids)
        category = offers[0].category
        template = loader.get_template('main/email_about_offers.html')
        result = template.render({'offers':offers},request)
        SendOfferEmail.delay(result, category)
        
    results = 'Please select a category from Filter.'
    categories = Category.objects.all()
    return render(request,'main/offer_page.html', {'categories':categories, 'results':results})
        
        
    




    

