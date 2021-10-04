import pyttsx3
import requests

from bs4 import BeautifulSoup

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = str(input("Paste article:\n"))
response = requests.get(text)
soup = BeautifulSoup(response.text, 'html.parser')
articles = []

for i in range(len(soup.select('.p'))):
    article = soup.select('.p')[i].getText().strip()
    articles.append(article)

text = " ".join(articles)
speak(text)

engine.runAndWait()