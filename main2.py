import vk_api
import course
import requests  

response1 = requests.get('https://swapi.dev/api/planets/').json() 
response2 = requests.get('https://swapi.dev/api/starships/').json()  
planets = response1.get('results')  
starships = response2.get('results')

token = 'vk1.a.9EA2thYMG9dPJKpmnlmDgzWRYwQ91_XejYDHT9NrA7mqXUE1ptrrsDBecLXyYur1V5vS0MWdjGUSXL3nIdEfYXntHv5u5tToZDdOUXqDozk0eXaqX0MXJr-rbJuK9j5A-lRB8uTHie5us-gEHQHlmk1ntfeI69_hHJKQ-CG7uaA-4DEslV6shQ6YT4sncnChDwnfAVc77U7z6l1-O3Ob8A'

vk = vk_api.VkApi(token=token)

maxdiameter = 0  
planetname = ''  
for i in range(10):  
    planetsD = planets[i].get('diameter')  
    if planetsD != "unknown":  
        diameter = int(planetsD)  
        if diameter > maxdiameter:  
            maxdiameter = diameter
            planetname = planets[i].get('name')  
                
max_atmosphering_speed = 0  
shipname = ''
for i in range(5):  
     speed_str = starships[i].get('max_atmosphering_speed')  
     if speed_str != "n/a":  
        speed = int(speed_str)  
        if speed > max_atmosphering_speed:  
            max_atmosphering_speed = speed  
            shipname = starships[i].get('name')  

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if 'привет' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Привет! Я умный бот, который скоро будет уметь делать много всего! Скорее подписывайся!'})
        elif '-к доллар' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': course.get_course('R01235')})
        elif '-к юань' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': course.get_course('R01375')})
        elif 'планеты' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': planetname})
        elif 'корабли' in message_text.lower():
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': shipname})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Я тебя не понимаю!'})