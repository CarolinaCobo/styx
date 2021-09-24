from django.shortcuts import render
from subscription.forms import EmailSignupForm
from subscription.models import Signup


def index(request):
    """
    A view to return the index page and take mailing list signups
    """
    form = EmailSignupForm()
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {"form": form}
    return render(request, "home/index.html", context)
