from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EmailSignupForm
from subscription.models import Signup

import json
import requests

url = 'https://api.convertkit.com/v3/forms/2675660/subscribe'


def subscribe(email):
    """
    View for handling sending the subscription to mailchimp
    """
    newData = {
        'api_key': settings.CONVERKIT_API_KEY,
        'email': email,
    }

    print(newData)
    headers = {'Content-type': 'application/json'}

    r = requests.post(
        url, data=json.dumps(newData), headers=headers
    )

    return r.json()


def email_list_signup(request):
    if request.method == 'POST':
        signUpForm = EmailSignupForm(request.POST or None)

        if signUpForm.is_valid():
            email = request.POST.get('email')
            response = subscribe(email)
            print("here_______")
            print(response)
            if response['subscription'] and response['subscription']['state'] == 'inactive':
                messages.info(
                    request, "Subscribed, please confirm your email.")
            elif response['subscription'] and response['subscription']['state'] == 'active':
                messages.info(
                    request, "Already subscribed, thanks for trying again!")
            else:
                messages.info(
                    request, "Something went wrong, please try again.")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
