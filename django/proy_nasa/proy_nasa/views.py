import requests
from django.shortcuts import render

def index(request):
    api_key = 'zQl9PdOIpAuGMBn9E9YIAiS0YuEOC7ZtLq7nlt6L'  
    api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&count=5'

    response = requests.get(api_url)
    data = response.json()

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
