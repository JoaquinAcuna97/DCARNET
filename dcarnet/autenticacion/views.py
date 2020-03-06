from django.shortcuts import render, redirect
from autenticacion.form import UsuarioForm, PerfilUsuarioForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carnets.views import create_person

# Create your views here.
def index(request):
    return render(request, "index.html")


@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("Estas Logeado, bien!")


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse("index"))


def register(request):

    registered = False

    if request.method == "POST":

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UsuarioForm(data=request.POST)
        profile_form = PerfilUsuarioForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if "profile_pic" in request.FILES:
                print("found it")
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES["profile_pic"]

            # Now save model
            profile.save()
            print("# Registration Successful!")
            print("# Creando una persona para este usuario!")
            create_person(user)
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UsuarioForm()
        profile_form = PerfilUsuarioForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    if registered:
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(
            request,
            "autenticacion/registration.html",
            {
                "user_form": user_form,
                "profile_form": profile_form,
                "registered": registered,
            },
        )


def user_login(request):

    if request.method == "POST":
        # First get the username and password supplied
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                if user.is_staff:
                    print("hello admin!")
                    return redirect("/admin/")
                else:
                    # Log the user in.
                    login(request, user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    #     print("hello user!" + user.usuario)
                    if user.usuario.tipo_usuario == "b":
                        print("hello doctor!" + user.username)
                        return redirect(reverse("index"), usuario=user.usuario)
                    if user.usuario.tipo_usuario == "a":
                        print("hello familiar!" + user.username)
                        return redirect(reverse("index"), usuario=user.usuario)
                    print("hello rare user with no type!" + user.usuario.tipo_usuario)
                    return redirect(reverse("index"), usuario=user.usuario)
            else:
                # If account is not active:
                messages.error(request, "Cuenta Desactivada.")
                return render(request, "autenticacion/login.html", {})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            messages.error(request, "Credeciales invalidas.")
            return render(request, "autenticacion/login.html", {})
    else:
        # Nothing has been provided for username or password.
        print("#Nothing has been provided for username or password.")
        return render(request, "autenticacion/login.html", {})
