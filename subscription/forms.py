from django import forms
from .models import Signup


class EmailSignupForm(forms.ModelForm):
    """
    Form for the mailing list signup
    """

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "id": "email",
                "placeholder": "Enter your email address",
            }
        ),
        label="",
    )

    class Meta:
        model = Signup
        fields = ("email",)
