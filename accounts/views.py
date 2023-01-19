from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import LoginForm, SignupForm
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("home")


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["password"] != form.cleaned_data["password_confirmation"]:
                form.add_error("password," "the passwords do not match")
                context = {"form": form}
                return render(request, "accounts/signup.html", context)
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"],
                )

                login(request, user)

                return redirect("home")
    else:
        form = SignupForm()
        context = {"form": form}
        return render(request, "accounts/signup.html", context)
