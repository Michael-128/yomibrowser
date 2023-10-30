from django.shortcuts import render, HttpResponse
from .dictionary_importer import import_dictionary
from .models import Dictionary

# Create your views here.
def dictionary_import(request):
    
    if request.method == "POST":
        print(request.FILES)
    
    #import_dictionary("./dictionaries/jmdict_english.zip")
    dictionaries = Dictionary.objects.all()

    return render(request, "import.html", {"dictionaries": dictionaries})