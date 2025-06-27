import requests
from django.http import HttpResponse
from datetime import datetime
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def luke_and_father(request):
    try:
        luke = requests.get('https://swapi.dev/api/people/1/', verify=False).json()
        vader = requests.get('https://swapi.dev/api/people/4/', verify=False).json()
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)

    html = f"""
    <h2>Luke Skywalker</h2>
    <p>Name: {luke['name']}</p>
    <p>Birth Year: {luke['birth_year']}</p>

    <h2>Darth Vader</h2>
    <p>Name: {vader['name']}</p>
    <p>Birth Year: {vader['birth_year']}</p>
    <p>Eye colour: {vader['eye_color']}</p>

    <hr>
    <p>Server Time: {datetime.now()}</p>
    """
    return HttpResponse(html)
