import requests
import json
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def latestNews():
    apidict= {"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=69dcc3ac5fb64dad8465953e66dd70b5",
              "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=69dcc3ac5fb64dad8465953e66dd70b5",
              "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=69dcc3ac5fb64dad8465953e66dd70b5",
              "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=69dcc3ac5fb64dad8465953e66dd70b5",
              "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=69dcc3ac5fb64dad8465953e66dd70b5"
              }
    content = None
    url = None
    speak("which field news do you want, [business] , [sports] , [entertainment] , [health] , [technology]")
    field= input("type field news that you want")
    for key, values in apidict.items():
        if key.lower() in field.lower():
            url=values
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")
    news = requests.get(url).text
    news = json.loads(news)
    speak("this is your first news")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles['url']
        print(f"for more info visit {news_url}")

        a = input("[press 1 to continue] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        speak("that's all")








