from django.shortcuts import render, get_object_or_404
from .models import D
# Create your views here.
def home(request):
    ds = D.objects
    return render(request, 'home.html', {'ds' : ds})
def detail(request, d_id):
    d_detail = get_object_or_404(D, pk = d_id)
    return render(request, 'detail.html', {'d' : d_detail})

