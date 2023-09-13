# Django framework
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Local application imports
from apps.users.forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm


def register(request):
    template_name = 'users/register.html'

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(
                request, f"Cuenta creada con éxito para {user.username}!!!, ya puedes ingresar")
            return redirect("login")
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, template_name, context)

@login_required
def profile(request):
    success_message = "Tu cuenta ha sido actualizada"

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile_obj = profile_form.save(commit=False)
            profile_obj.save()
            messages.success(
                request, success_message)
            return redirect("profile-account")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    # pdb.set_trace()
    return render(request, 'users/profile.html', context)
