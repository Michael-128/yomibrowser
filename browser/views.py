from django.shortcuts import render, HttpResponse
from dictionaries.models import Term, Dictionary
from django.db.models import Q, Count, Avg
from django.db.models.functions import Length


# Create your views here.
def home(request):
    terms = Term.objects.none()
    
    if request.GET:
        keyword = request.GET["term"]
        terms = Term.objects.all().filter(Q(term__startswith=keyword) | Q(reading__startswith=keyword)).annotate(accuracy=Avg(Length("term")+Length("reading")-(len(keyword)*2))).order_by("accuracy", "-popularity")

    return render(request, "home.html", {"terms": terms})