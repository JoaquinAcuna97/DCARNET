from django.shortcuts import render, redirect
from autenticacion.form import UsuarioForm, PerfilUsuarioForm, LoginForm
from autenticacion.models import Usuario
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
        usuario_form = PerfilUsuarioForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and usuario_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            usuario = usuario_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserusuarioInfoForm
            usuario.user = user

            # Check if they provided a usuario picture

            if "foto_perfil" in request.FILES:
                print("Encontramos la foto")
                # If yes, then grab it from the POST form reply
                usuario.foto_perfil = request.FILES["foto_perfil"]

            # Now save model
            usuario.save()
            print("# Registration Successful!")

            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors, usuario_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UsuarioForm()
        usuario_form = PerfilUsuarioForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    if registered:
        login(request, user)

        usuario = Usuario.objects.get(user_id=user.pk)

        if usuario:
            if user.usuario.tipo_usuario == "b":
                return HttpResponseRedirect(reverse("carnets:crear_medico"))
            elif user.usuario.tipo_usuario == "a":
                return HttpResponseRedirect(reverse("carnets:crear_familiar"))
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(
            request,
            "autenticacion/registration.html",
            {
                "user_form": user_form,
                "profile_form": usuario_form,
                "registered": registered,
            },
        )


def user_login(request):

    if request.method == "POST":
        print("post login")
        login_form = LoginForm(data=request.POST)
        print("login form")
        if login_form.is_valid():
            print("VALID")
            # First get the username and password supplied
            username = request.POST.get("username")
            password = request.POST.get("password")

            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)

            # If we have a user
            if user:

                messages.info(
                    request, "",
                )
                if user.is_active:
                    if user.is_staff:
                        messages.success(
                            request, "", extra_tags="alert alert-success"
                        )  # <-
                        print("hello admin!")
                        return redirect("/admin/")
                    else:


                        usuario = Usuario.objects.get(user_id=user.pk)
                        # Log the user in.
                        login(request, user)
                        messages.success(request, "Hello !")  # <-
                        # Send the user back to some page.

                        from carnets.models import Medico, Tutor
                        if usuario:
                            if user.usuario.tipo_usuario == "b":
                                messages.success(request, "Hola doctor!")
                                medico = Medico.objects.get(usuario_id=user.usuario.pk)
                                if not medico:
                                    messages.success(request, "Complete perfil!")
                                    return HttpResponseRedirect(reverse("carnets:crear_medico"))
                            elif user.usuario.tipo_usuario == "a":
                                messages.success(request, "Hola tutor!")
                                tutor = Tutor.objects.get(usuario_id=user.usuario.pk)
                                if not tutor:
                                    messages.success(request, "Complete perfil!")
                                    return HttpResponseRedirect(reverse("carnets:crear_familiar"))



                        # In this case their homepage.
                        return HttpResponseRedirect(reverse("index"))
                else:
                    # If account is not active:
                    messages.error(request, "Cuenta Desactivada.")
                    return render(request, "autenticacion/login.html", {})
            else:
                print("Someone tried to login and failed.")
                print(
                    "They used username: {} and password: {}".format(username, password)
                )
                messages.error(
                    request, "Credeciales invalidas.", extra_tags="alert alert-danger"
                )
                return render(
                    request, "autenticacion/login.html", {"login_form": login_form,},
                )
        else:
            # One of the forms was invalid if this else gets called.
            print("INVALID")
            print(login_form.errors)
            return render(
                request, "autenticacion/login.html", {"login_form": login_form,},
            )

    else:
        # Nothing has been provided for username or password.
        print("#Carga de login.")
        # Was not an HTTP post so we just render the forms as blank.
        login_form = LoginForm()
        return render(request, "autenticacion/login.html", {"login_form": login_form})
