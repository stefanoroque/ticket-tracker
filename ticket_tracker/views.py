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
from .forms import NewRegisterForm

# Create your views here.

def index(request):
    return render(request, "ticket_tracker/index.html")

def signin_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "ticket_tracket/signin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "ticket_tracker/signin.html")

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

            print(username)
            print(first_name)
            print(last_name)
            print(email)
            print(role)
            print(password)
            print(confirmation)

            return render(request, "ticket_tracker/register.html", {
                "form": NewRegisterForm()
            })
        

            # Redirect user to list of tasks
            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            
            # If the form is invalid, re-render the page with existing information.
            return render(request, "ticket_tracker/register.html", {
                "form": register_form
            })







        # username = request.POST["username"]
        # first_name = request.POST["first_name"]
        # last_name = request.POST["last_name"]
        # email = request.POST["email"]
        # role = request.POST["role"]
        # password = request.POST["password"]
        # confirmation = request.POST["confirmation"]

        

        # # Ensure that all of the form fields are filled out
        # for entry in request.POST:
        #     if request.POST[entry] == '':
        #         return render(request, "ticket_tracker/register.html", {
        #         "message": "All form fields must be filled in."
        #     })

        # # Ensure password matches confirmation
        # if password != confirmation:
        #     return render(request, "ticket_tracker/register.html", {
        #         "message": "Passwords must match."
        #     })

        # Attempt to create new user
        try:
            pass
            #user = User.objects.create_user(username, email, password)
            # user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        # login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "ticket_tracker/register.html", {
                "form": NewRegisterForm()
            })