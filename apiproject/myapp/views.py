import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    city_data = None
    city_list = None

    if request.method == 'POST':
        state = request.POST.get('state')
        country = request.POST.get('country')
        city = request.POST.get('city')

        YOUR_API_KEY = '31b55c52-7915-491e-b692-7df26bd172ba'

        # if not city:
            # Step 1: Retrieve the list of cities based on state and country
        city_list_url = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=city_list_url)
        city_list = r.json()
    # else:
        # Step 2: Retrieve city-specific air quality data
        city_data_url = f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=city_data_url)
        city_data = r.json()

    return render(request, 'airapp/index.html', {'city_list': city_list, 'city_data': city_data})
