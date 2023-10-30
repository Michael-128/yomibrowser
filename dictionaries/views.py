from django.shortcuts import render, HttpResponse
from .dictionary_importer import import_dictionary

# Create your views here.
def dictionary_import(request):
    
    
    
    #import_dictionary("./dictionaries/jmdict_english.zip")

    return render(request, "import.html")