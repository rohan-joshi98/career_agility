from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'dashboard/new_LANDING PAGE.html')

def strategy(request):
    return render(request,'dashboard/strategy_page_bs.html')

def brand(reqest):
    return render(reqest, 'dashboard/brand_bs.html')

def operations(request):
    return render(request, 'dashboard/operations_bs.html')

def people(request):
    return render(request, 'dashboard/people_bs.html')