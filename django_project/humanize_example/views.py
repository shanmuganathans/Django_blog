from django.shortcuts import render
from django.utils import timezone

import datetime

current_time = datetime.datetime.now()

# Create your views here.

def index(request):
    context = {
        "current_date": timezone.now(),
        "large_number": 98765678756,
        "ordinal_number": 100,
        "current_time": current_time,
        "day1" : current_time + datetime.timedelta(days=367),
        
    }
    return render(request, "humanize_example/index.html", context)