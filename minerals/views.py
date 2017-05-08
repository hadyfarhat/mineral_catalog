from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def minerals_list(request):
    return render(request, "minerals/index.html")