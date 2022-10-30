import numpy as np
import pandas as pd
from django.shortcuts import render, redirect
from .models import *
from secret import *

def test(request):
    context = {
        'key' : MAP_APP_KEY
    }
    return render(request, "main/test.html", context)


def index(request):
    bs = BusInfo.objects.all()
    context = {
        'bus' : bs,
        'key' : MAP_APP_KEY
    }
    return render(request, "main/index.html", context)