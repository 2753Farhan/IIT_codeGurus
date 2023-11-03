import requests
from django.shortcuts import render

def index(request):
    YOUR_API_KEY = '31b55c52-7915-491e-b692-7df26bd172ba'
    URL = f'http://api.airvisual.com/v2/city?city=Los%20Angeles&state=California&country=USA&key={YOUR_API_KEY}'
    
    r = requests.get(url=URL)
    res = r.json()
    return render(request, 'airapp/index.html', {'response': res})