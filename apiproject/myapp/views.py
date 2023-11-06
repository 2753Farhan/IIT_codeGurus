import requests
from django.shortcuts import render


def step1(request):
    city_list = None
    state = ''
    country = ''
    if request.method == 'POST':
        state = request.POST.get('state')
        country = request.POST.get('country')
        YOUR_API_KEY = 'c875f965-df7b-4d10-a957-14654b35a017'

        # Step 1: Retrieve the list of cities based on state and country
        city_list_url = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=city_list_url)
        city_list = r.json()
        # Remove leading/trailing spaces from 'state' and 'country'
    state = state.strip()
    country = country.strip()

# Rest of your code

    return render(request, 'airapp/step1.html', {'city_list': city_list, 'state' : state, 'country' : country})

def step2(request, state, country, selected_city):
    city_data = None

    YOUR_API_KEY = 'c875f965-df7b-4d10-a957-14654b35a017'

    # Step 2: Retrieve city-specific air quality data
    city_data_url = f'http://api.airvisual.com/v2/city?city={selected_city}&state={state}&country={country}&key={YOUR_API_KEY}'
    r = requests.get(url=city_data_url)
    city_data = r.json()

    return render(request, 'airapp/step2.html', {'city_data': city_data})
def index(request):
    city_data = None
    city_list = None

    if request.method == 'POST':
        state = request.POST.get('state')  # Get user input for state
        country = request.POST.get('country')  # Get user input for country

        YOUR_API_KEY = 'c875f965-df7b-4d10-a957-14654b35a017'
        URL = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=URL)
        res = r.json()
        city_data = []

        for city_entry in res.get('data', []):
            city_name = city_entry.get('city')
            if city_name:
                city_list_url = f'http://api.airvisual.com/v2/city?city={city_name}&state={state}&country={country}&key={YOUR_API_KEY}'
                r = requests.get(url=city_list_url)
                city_data_entry = r.json()

                current_data = city_data_entry.get('data', {}).get('current', {})
                if 'pollution' in current_data:
                    aqius_value = current_data['pollution'].get('aqius', 'N/A')
                else:
                    aqius_value = 'N/A'

                city_data.append({'city': city_name, 'aqius': aqius_value})

        if city_data:
            city_list = sorted(city_data, key=lambda x: x['aqius'])

        return render(request, 'airapp/index.html', {'city_list': city_list, 'state': state, 'country': country})

    return render(request, 'airapp/index.html', {'city_list': None})

def dynamic_marker(request):
    return render(request, 'airapp/dynamic_marker.html')