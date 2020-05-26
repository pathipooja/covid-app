from django.shortcuts import render
import requests
from .models import Country
from .forms import CountryForm


def index(request):
    # url='https://api.covid19api.com/live/country/{}'
    # url = 'http://covid19-india-adhikansh.herokuapp.com/state/{}'
    url = 'https://coronavirus-19-api.herokuapp.com/countries/{}'
    if request.method == 'POST':
        form = CountryForm(request.POST)
        res = form.data['name']
        form.save()

    form = CountryForm()
    countries = Country.objects.all()
    country_data = []
    i = 0
    for country in countries:
        i += 1
        r = requests.get(url.format(country))
        if r.status_code == 200:
            if r.text == "Country not found":
                res = "Invalid input"
                continue
            else:
                res = ""
            r = r.json()
            country_status = {
                'country': country.name,
                'confirmed_cases': r['cases'],
                'death_cases': r['deaths'],
                'recovered_cases': r['recovered'],
                'active_cases': r['active'],
            }

    country_data.append(country_status)
    '''else:
            country_status = {
                'country': " ",
                'confirmed_cases': 0,
                'death_cases': 0,
                'recovered_cases': 0,
                'active_cases': 0,
            }
'''
    if i == 0:
        context = {'form': form}
    elif request.method == 'POST':
        context = {'country_data': country_data, 'res': res, 'form': form}
    else:
        context = {'country_data': country_data, 'res': 'Last Search', 'form': form}
    return render(request, 'covid_status/covid_status.html', context)
