import pyaudio
import speech_recognition as sr
while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь...')
        audio = r.listen(source)

    speech = r.recognize_google(audio, language='ru_RU').lower()
    print('Вы сказали:', speech)
    if speech == 'привет':
        print('Привет')