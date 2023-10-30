from django.shortcuts import render, HttpResponse
from dictionaries.models import Term, Dictionary
from django.db.models import Q, Count, Avg, Max, Case, F, Value, When, QuerySet
from django.db.models.functions import Length

import re, json

def roman_definitions_filter(term: Term):
    pattern = "^[a-zA-Z]+$"
    
    defs = json.loads(term.definitions)

    for index, definition in enumerate(defs):
        if re.match(pattern, definition) and definition == term.keyword:
            term.position = index
            return True
        
    return False

# Create your views here.
def home(request):
    terms = Term.objects.none()
    
    if request.GET:
        keyword = request.GET["term"]

        filtered = filter(roman_definitions_filter, Term.objects.all().filter(definitions__contains=keyword).annotate(keyword=Value(keyword), position=Value(999)))
        
        terms = list(filtered)


        terms += Term.objects.all().filter(Q(term__startswith=keyword) | Q(reading__startswith=keyword)).annotate(reading_exact=Case(When(reading=keyword, then=Value(True))), term_exact=Case(When(term=keyword, then=Value(True)))).order_by("-term_exact", "-reading_exact", "-popularity")

    return render(request, "home.html", {"terms": terms})