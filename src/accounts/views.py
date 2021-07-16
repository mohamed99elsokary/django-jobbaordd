from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from .models import *


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/accounts/profile")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context=context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {"profile": profile}
    return render(request, "accounts/profile.html", context=context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profile = profileform.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(reverse("accounts:profile"))

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {"userform": userform, "profileform": profileform}
    return render(request, "accounts/profile_edit.html", context)
