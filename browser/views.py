from django.shortcuts import render, HttpResponse
from dictionaries.models import Term, Dictionary
from django.db.models import Q, Count, Avg, Max, F
from django.db.models.functions import Length

import re, json

# Create your views here.
def home(request):
    terms = Term.objects.none()
    
    if request.GET:
        keyword = request.GET["term"]

        match = re.match("^[a-zA-Z]*$", keyword)
        print(match)

        if match:
            terms = Term.objects.all().filter(definitions__contains=keyword).order_by("popularity")
        else:
            terms = Term.objects.all().filter(Q(term__startswith=keyword) | Q(reading__startswith=keyword)).annotate(accuracy=Avg(Length("term")+Length("reading")-(len(keyword)*2))).order_by("accuracy", "-popularity")

    return render(request, "home.html", {"terms": terms, "keyword": request.GET["term"]})