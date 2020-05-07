from django.shortcuts import render
from requests import get
from .models import Country
from .forms import CountryForm


def index(request):
    # url='https://api.covid19api.com/live/country/{}'
    url = 'http://covid19-india-adhikansh.herokuapp.com/state/{}'

    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['name']
        print(a)
        # data = request.POST.get('name')
        # form.save()
        r = get(url.format(a))
        if r.status_code == 200:
            form.save()
            r = r.json()
            # print(r.text)
            country_status = {
                'country': a,
                'confirmed_cases': r['data'][0]['total'],
                'death_cases': r['data'][0]['death'],
                'recovered_cases': r['data'][0]['cured'],
                'active_cases': r['data'][0]['confirmed'],
            }
            print(country_status)
            context = {'country_status': country_status, 'form': form}
            return render(request, 'covid_status/covid_status.html', context)

    form = CountryForm()
    countries = Country.objects.all()
    obj = Country.objects.filter().latest('id')
    print(obj)
    context = {'form': form}
    return render(request, 'covid_status/covid_status.html', context)
