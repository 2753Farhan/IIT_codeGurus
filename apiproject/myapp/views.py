import requests
from django.shortcuts import render


def step1(request):
    state = 'bjs'
    country = 'hbchs'
    city_list = None

    if request.method == 'POST':
        state = request.POST.get('state')
        country = request.POST.get('country')
        YOUR_API_KEY = 'e5ce7c06-2258-464a-b998-1ad1cf1a0ba0'

        # Step 1: Retrieve the list of cities based on state and country
        city_list_url = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=city_list_url)
        city_list = r.json()

    return render(request, 'airapp/step1.html', {'city_list': city_list, 'state' : state, 'country' : country})

def step2(request, state, country, selected_city):
    city_data = None

    YOUR_API_KEY = 'e5ce7c06-2258-464a-b998-1ad1cf1a0ba0'

    # Step 2: Retrieve city-specific air quality data
    city_data_url = f'http://api.airvisual.com/v2/city?city={selected_city}&state={state}&country={country}&key={YOUR_API_KEY}'
    r = requests.get(url=city_data_url)
    city_data = r.json()

    return render(request, 'airapp/step2.html', {'city_data': city_data})

