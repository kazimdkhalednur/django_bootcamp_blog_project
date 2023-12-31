from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from .forms import RegistrationForm, CustomAuthenticationForm
from .models import User


def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, "accounts/registration_success.html")
    context = {
        "forms": form,
        "title": "Registration"
    }
    return render(request, "accounts/registration.html", context)


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "title": "Sign In"
            }
        )
        return context
        

def signout(request):
    logout(request)
    return redirect("blogs:home")

