from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from marketingforhackers.landingpage.models import Lead

def index(request):
    # try to figure out where they came from
    try:
        referrer = request.META.HTTP_REFERER
    except AttributeError:
        referrer = "direct"
        
    analytics = {"referrer": referrer}
    
    return render_to_response("index.html", analytics, context_instance=RequestContext(request))
    
def submit(request):
    # grab info
    email = request.POST['email']
    referrer = request.POST['referrer']
    
    # save locally
    lead_to_submit = Lead(email=email, referrer=referrer)
    lead_to_submit.save()
    
    # send to Mailchimp
    
    
    return  HttpResponseRedirect(reverse('landingpage.views.thanks'))
    
def thanks(request):
    return render_to_response("thanks.html")
    