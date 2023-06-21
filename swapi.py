import requests  
  
response = requests.get('https://swapi.dev/api/starships/').json()  
starships = response.get('results')  
  
max_atmosphering_speed = 0  
ship_name = ''  
for i in range(5):  
    speed_str = starships[i].get('max_atmosphering_speed')  
    if speed_str != "n/a":  
        speed = int(speed_str)  
        print(f"{starships[i].get('name')} - {speed}")  
        if speed > max_atmosphering_speed:  
            max_atmosphering_speed = speed  
            ship_name = starships[i].get('name')  
  
print("Fastest is ",ship_name)