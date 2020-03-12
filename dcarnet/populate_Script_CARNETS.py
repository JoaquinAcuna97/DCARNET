import os
import urllib.request
from bs4 import BeautifulSoup
import sys
import requests
import urllib.request
import tempfile
from django.core import files

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dcarnet.settings")

import django

# Import settings
django.setup()

import random
from carnets.models import Nino
from faker import Faker

fakegen = Faker()
tipo = ["tutor", "Doctor", "Nino"]


def Create_nino(nombre):
    """
    Create N Entries of Dates Accessed
    """
    nino = Nino.objects.get_or_create(
        tipo_persona="c",
        nombre=nombre.split(" ")[0],
        apellido=nombre.split(" ")[-1],
        fecha_de_nacimiento=fakegen.date(),
        documento_de_Identidad=fakegen.random_number(digits=None, fix_len=False),
        lugar_de_nacimiento=fakegen.city(),
    )[0]
    print("Created nino" + nino.nombre)
    return nino


#!{sys.executable} -m pip install beayutifulsoup4


# url = input('Enter img ulr to download:')

# file_name= input('enter a filename to save as')


# dl_jpg(url, 'images/',file_name)


# datos = urllib.request.urlopen("rugrats.html").read().decode()
def populateNinos():

    f = open("rugrats.html", encoding="utf8")
    soup = BeautifulSoup(f)
    images = soup.find_all("img")

    for image in images:
        print("nombre: " + image.get("alt"))
        image_url = image.get("src")
        # Steam the image from the url
        request = requests.get(str(image_url), stream=True)

        # Was the request OK?
        if request.status_code != requests.codes.ok:
            # Nope, error handling, skip file etc etc etc
            continue
            print("ERROR")
        print("Good")
        # Get the filename from the url, used for saving later
        file_name = image_url.split("/")[-1]
        print("file name " + file_name)
        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in request.iter_content(1024 * 8):

            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)

        # Create the model you want to save the image to
        nino = Create_nino(image.get("alt"))
        print("Created nino")
        # Save the temporary image to the model#
        # This saves the model so be sure that is it valid
        nino.foto_perfil.save(image.get("alt"), files.File(lf))


if __name__ == "__main__":
    print("Populating the databases...Please Wait")
    populateNinos()
    print("Populating Complete")
