import requests
from django.shortcuts import render

def city_detail(request, state, country, city):
    city_data = None
    YOUR_API_KEY = '31b55c52-7915-491e-b692-7df26bd172ba'

    city_data_url = f'http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={YOUR_API_KEY}'
    r = requests.get(url=city_data_url)
    city_data = r.json()

    return render(request, 'airapp/city_detail.html', {'city_data': city_data})
