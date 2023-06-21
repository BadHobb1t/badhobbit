import requests  
  
response = requests.get('https://swapi.dev/api/planets/').json()  
planets = response.get('results')  
  
maxdiameter = 0  
planetname = ''  
for i in range(10):  
    planetsD = planets[i].get('diameter')  
    if planetsD != "unknown":  
        diameter = int(planetsD)  
        if diameter > maxdiameter:  
            maxdiameter = diameter  
            planetname = planets[i].get('name')  
  
print(planetname, maxdiameter)