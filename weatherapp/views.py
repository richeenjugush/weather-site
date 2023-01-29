from django.shortcuts import render
import json
import urllib.request 

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city'].capitalize()
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=2d9573fad51edd8ff0d95a9549b07742&units=metric').read()
        json_data = json.loads(res)       
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        data = ''
        city = ''
    return render(request, 'index.html',{'city':city, 'data':data}) 