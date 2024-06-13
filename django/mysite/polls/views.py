import requests
from django.shortcuts import render

def index(request):
    api_key = 'DEMO_KEY'  # Reemplaza con tu API Key de la NASA
    api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=5'

    response = requests.get(api_url)
    data = response.json()

    # Extrae los datos relevantes
    programas = []
    for item in data:
        programas.append({
            'title': item['title'],
            'date': item['date'],
            'explanation': item['explanation'],
            'url': item['url']
        })

    context = {'programas': programas}
    return render(request, 'nasa_app/index.html', context)
