from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EmailSignupForm
from subscription.models import Signup

import json
import requests

url = 'https://api.convertkit.com/v3/forms/2632824/subscribe'


def subscribe(email):
    """
    View for handling sending the subscription to mailchimp
    """
    print(email)
    newData = {
        'api_key': 'H8BbA--hjpsNGhtZYLEncQ',
        'email': "niall@codu.ie",
    }
    headers = {'Content-type': 'application/json'}

    # data = {"email_address": email, "status": "subscribed"}
    r = requests.post(
        url, data=json.dumps(newData), headers=headers
    )
    print("here _______")
    print(r.json())
    return r.status_code, r.json()


def email_list_signup(request):
    """
    Checks if user is signed up and if not sends the email address to mailchimp
    """
    print("+++++++")
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    print(body)
    form = EmailSignupForm(request.POST or None)
    subscribe(form.instance.email)
    # if request.method == "POST":
    #     if form.is_valid():
    #         email_signup_qs = Signup.objects.filter(email=form.instance.email)
    #         if email_signup_qs.exists():
    #             messages.info(request, "You are already subscribed")
    #         else:
    #             subscribe(form.instance.email)
    #             form.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
