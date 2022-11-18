import requests
a = input()
s_city="Moscow,Ru"
appid="c9a19e4e0a8a72132ecf2e04aeacff8d"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
    params={'q': s_city,'units':'metric','lang':'ru','APPID': "c9a19e4e0a8a72132ecf2e04aeacff8d"})
data = res.json()
if a=='today':
    print("Прогноз погоды на сегодня:")
    print("Город:", s_city)
    print("Погодные условия:", data['weather'][0]['description'])
    print("Температура:", data['main']['temp'])
    print("Минимальная температура:", data['main']['temp_min'])
    print("Максимальная температура", data['main']['temp_max'])
    print("Скорость ветра:", data['wind']['speed'])
    print("Видимость:", data['visibility'])
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
    params={'q': s_city,'units':'metric','lang':'ru','APPID': "c9a19e4e0a8a72132ecf2e04aeacff8d"})
data = res.json()
if a=='week':
    print("Прогноз погоды на неделю:")
    print("Город:", s_city)
    for i in data['list']:
        print("Дата <", i['dt_txt'],
            "> \r\nТемпература<",'{0:+3.0f}'.format(i['main']['temp']),
            "> \r\nПогодные условия <",i['weather'][0]['description'],
            "> \r\nСкорость ветра <",i['wind']['speed'],
            "> \r\nВидимость <",i['visibility'],">")
        print("____________________________")