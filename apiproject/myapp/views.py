import requests
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        state = request.POST.get('state')  # Get user input for state
        country = request.POST.get('country')  # Get user input for country
        YOUR_API_KEY = '31b55c52-7915-491e-b692-7df26bd172ba'
        URL = f'http://api.airvisual.com/v2/cities?state={state}&country={country}&key={YOUR_API_KEY}'
        r = requests.get(url=URL)
        res = r.json()
        return render(request, 'airapp/index.html', {'response': res, 'state': state, 'country': country})
    return render(request, 'airapp/index.html', {'response': None})
