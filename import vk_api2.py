import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = 'vk1.a.9EA2thYMG9dPJKpmnlmDgzWRYwQ91_XejYDHT9NrA7mqXUE1ptrrsDBecLXyYur1V5vS0MWdjGUSXL3nIdEfYXntHv5u5tToZDdOUXqDozk0eXaqX0MXJr-rbJuK9j5A-lRB8uTHie5us-gEHQHlmk1ntfeI69_hHJKQ-CG7uaA-4DEslV6shQ6YT4sncnChDwnfAVc77U7z6l1-O3Ob8A'

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print(event.text)
        print(event.user_id)
        print(event.datetime)
        print(event.to_me)
        