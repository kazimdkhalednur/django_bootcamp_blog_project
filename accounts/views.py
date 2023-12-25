from django.shortcuts import render

from .forms import RegistrationForm
from .models import User


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/registration_success.html")
    context = {
        "form": form
    }
    return render(request, "accounts/registration.html", context)
        
