from django.shortcuts import render
from django.conf import settings
import json
import urllib.request
from django.core.exceptions import ImproperlyConfigured

def index(request):
    data = {}
    error_message = ''
    if request.method == 'POST':
        city = request.POST['city'].capitalize()
        try:
            api_key = settings.OPENWEATHERMAP_API_KEY  # Access the API key from settings
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            res = urllib.request.urlopen(url).read()
            json_data = json.loads(res)
            if json_data.get('cod') != 200:
                error_message = json_data.get('message', 'Error fetching weather data')
            else:
                data = {
                    "country_code": str(json_data['sys']['country']),
                    "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
                    "temp": str(json_data['main']['temp']),
                    "pressure": str(json_data['main']['pressure']),
                    "humidity": str(json_data['main']['humidity']),
                    "wind": str(json_data['wind']['speed']),
                    "description": str(json_data['weather'][0]['description']),
                    # "description": "rain",
                    "city": city
                }
        except urllib.error.HTTPError as e:
            error_message = f"HTTP error occurred: {e.reason}"
        except urllib.error.URLError as e:
            error_message = f"URL error occurred: {e.reason}"
        except ImproperlyConfigured as e:
            error_message = str(e)
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
    
    return render(request, 'index.html', {'data': data, 'error_message': error_message})
