# Django framework
from django.contrib import messages
from django.shortcuts import redirect, render

# Local application imports
from apps.users.forms import UserRegisterForm


def register(request):
    template_name = 'users/register.html'

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(
                request, f"Cuenta creada con éxito para {user.username}")
            return redirect("home-page")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, template_name, context)
