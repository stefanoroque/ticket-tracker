import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import NewRegisterForm, NewSigninForm

# Create your views here.

def index(request):
    return render(request, "ticket_tracker/index.html")

def signin_view(request):
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        signin_form = NewSigninForm(request.POST)

        # Check if form data is valid (server-side)
        if signin_form.is_valid():

            # Isolate the data from the 'cleaned' version of the form
            username = signin_form.cleaned_data["username"]
            password = signin_form.cleaned_data["password"]

            # Attempt to sign user in
            user = authenticate(request, username=username, password=password)

            # Check if authentication successful
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "ticket_tracker/signin.html", {
                    "message": "Invalid username and/or password.",
                    "form": signin_form
                })
        
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "ticket_tracker/signin.html", {
                "form": signin_form
            })

    else:
        return render(request, "ticket_tracker/signin.html", {
                "form": NewSigninForm()
            })

def register(request):
    #TODO: have this function create a new user in the database
    if request.method == "POST":

        # Take in the data the user submitted and save it as form
        register_form = NewRegisterForm(request.POST)

        # Check if form data is valid (server-side)
        if register_form.is_valid():

            # Isolate the data from the 'cleaned' version of the form
            username = register_form.cleaned_data["username"]
            first_name = register_form.cleaned_data["first_name"]
            last_name = register_form.cleaned_data["last_name"]
            email = register_form.cleaned_data["email"]
            role = register_form.cleaned_data["role"]
            password = register_form.cleaned_data["password"]
            confirmation = register_form.cleaned_data["confirmation"]

            # Ensure password matches confirmation
            if password != confirmation:
                return render(request, "ticket_tracker/register.html", {
                    "message": "Passwords must match.",
                    "form": register_form
                })

            # Attempt to create new user
            try:
                user = User.objects.create_user(username=username, 
                                                first_name=first_name, 
                                                last_name=last_name,
                                                email=email,
                                                role=role,
                                                password=password)
                user.save()
            except IntegrityError:
                return render(request, "ticket_tracker/register.html", {
                    "message": "Username already taken.",
                    "form": register_form
                })

            return render(request, "ticket_tracker/signin.html", {
                "message": "You have successfully registered an account."
            })


        else:
            
            # If the form is invalid, re-render the page with existing information.
            return render(request, "ticket_tracker/register.html", {
                "form": register_form
            })


    else:
        return render(request, "ticket_tracker/register.html", {
                "form": NewRegisterForm()
            })

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))