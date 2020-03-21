from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from django.http import HttpResponse
from dashboard.models import Indicators
from dashboard.forms import Indicators_Form


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

def indicators(request):
    indicator_list=Indicators.objects.order_by('user')
    indi_dict={'indi_list':indicator_list}
    return render(request, 'tables/indicators.html',context=indi_dict)


def indicators_form(request):
    form = Indicators_Form()
    if request.method == 'POST':
        form = Indicators_Form(request.POST)
        if form.is_valid():
            form.save()
            indicators = form.cleaned_data['indicators']
            page= form.cleaned_data['page']
            user= form.cleaned_data['user']
            return redirect('indicators')
        else:
            print('ERROR')
    else:
        form = Indicators_Form(request.GET)
        if form.is_valid():
            form.save()
            indicators = form.cleaned_data['indicators']
            page= form.cleaned_data['page']
            user= form.cleaned_data['user']
            return redirect('indicators')
        else:
            print('error')
    return render(request, 'tables/indi_form.html', {'form': form})

def recommendation_form(request):
    return render(request,"tables/recomm.html")





