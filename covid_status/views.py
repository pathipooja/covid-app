from django.shortcuts import render
from requests import get
from .models import Country
from .forms import CountryForm


def index(request):
    # url='https://api.covid19api.com/live/country/{}'
    url = 'http://covid19-india-adhikansh.herokuapp.com/state/{}'

    if request.method == 'POST':
        form = CountryForm(request.POST)
        a = form['name'].value()
        print(a)
        # form.save()
        r = get(url.format(a))
        if r.status_code == 200:
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

    '''countries=Country.objects.all()
    each_country=[]
    for country in countries:

        r=requests.get(url.format(country)).json()
        #print(r.text)
        country_status={
            'country' :country.name,
            'confirmed_cases':r['data'][0]['total'],
            'death_cases': r['data'][0]['death'],
            'recovered_cases':r['data'][0]['cured'],
            'active_cases': r['data'][0]['confirmed'],
        }
        each_country.append(country_status)
    print(each_country)
    context={'each_country':each_country,'form':form}
    '''

    form = CountryForm()
    context = {'form': form}
    return render(request, 'covid_status/covid_status.html', context)
