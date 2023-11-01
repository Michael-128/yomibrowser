from django.shortcuts import render, HttpResponse
from .dictionary_importer import import_dictionary
from .models import Dictionary
from .forms import DictionaryUploadForm

import io

# Create your views here.
def dictionary_import(request):
    
    form = DictionaryUploadForm()

    if request.method == "POST":
        form = DictionaryUploadForm(request.POST, request.FILES)   
        if form.is_valid(): 
            import_dictionary(form.files["dictionary"])
    
    #import_dictionary("./dictionaries/jmdict_english.zip")
    dictionaries = Dictionary.objects.all()

    return render(request, "import.html", {"dictionaries": dictionaries, "dict_form": form})