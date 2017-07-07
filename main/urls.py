from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^offers', views.offers, name='offers'),
    url(r'^company/(?P<comp_name>[a-zA-Z]+)$',views.company, name='company'),
    url(r'^category/(?P<cat_name>[a-zA-Z-]+)$',views.category, name='category'),
    url(r'^shop/(?P<offer_id>[0-9]+)$', views.shop, name='shop'),
    url(r'^mailoffers', views.mailoffers, name='mailoffers'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^addBankDetails$', views.addBankDetails, name='addBankDetails'),
    url(r'^addPaytmDetails$', views.addPaytmDetails, name='addPaytmDetails'),
    url(r'^setCategoryPrefs$', views.setCategoryPrefs, name='setCategoryPrefs'),
    url(r'^contact$', views.contact, name="contact"),
    url(r'^terms$', views.terms, name="terms"),
]
