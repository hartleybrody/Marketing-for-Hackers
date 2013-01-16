from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse

from marketingforhackers.landingpage.models import Lead
from mailsnake import MailSnake
from marketingforhackers import settings


def index(request):
    # try to figure out where they came from
    referrer = request.META.get('HTTP_REFERER')
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
    key = settings.MAILCHIMP_API_KEY
    list_num = settings.MAILCHIMP_LIST_NUM

    # see: http://www.nerdydork.com/integrate-mailchimp-with-your-django-app.html
    mailsnake = MailSnake(key)
    try:
        mailsnake.listSubscribe(
            id=list_num,
            email_address=email,
            double_optin=False,
            send_welcome=True
        )
    except:
        pass

    return HttpResponseRedirect(reverse('landingpage.views.thanks'))


def thanks(request):
    return render_to_response("thanks.html")


def author(request):
    import hashlib, urllib

    #get gravatar URL, from: http://en.gravatar.com/site/implement/images/python/
    email = "hartley.brody@gmail.com"
    size = 150
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'s': str(size)})

    author_info = dict(thumbnail=gravatar_url)

    return render_to_response("author.html", author_info)


def view_leads(request):
    if not request.GET.get("pass") == settings.VIEW_LEADS_PASSWORD:
        return HttpResponse("those are private", status=403)

    all_leads = Lead.objects.order_by('id').reverse()
    total = len(all_leads)

    return render_to_response("dump.html", dict(leads=all_leads, total=total))
