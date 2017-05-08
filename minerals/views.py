from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Mineral

# Create your views here.
def minerals_list(request):
    minerals = Mineral.objects.all()
    return render(request, "minerals/mineral_list.html", {'minerals': minerals})


def mineral_details(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, "minerals/mineral_details.html",
                  {'mineral': mineral})