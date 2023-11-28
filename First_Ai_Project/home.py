from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
activationWord = 'metron'

chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def search_wikipedia(text = ''):
    searchResults = wikipedia.search(text)
    print(searchResults)
    if not searchResults:
        print('No wikipedia results')
        return 'No result recieved'
    try:
        wikiPage = wikipedia.page(searchResults[1])
    except wikipedia.DisambiguationError as err:
        wikiPage = wikipedia.page(err.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.pause_threshold = 2
        user_speech = recognizer.listen(mic)
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
    try:
        text = recognizer.recognize_google(user_speech, language="en-US")
        return text
    except Exception as err:
        speak("I didn't catch that")


if __name__ == '__main__':
    speak("All systems opporating.")
    while True:
        text = parseCommand().lower().split()
        if text[0] == activationWord:
            print(text)
            text.pop(0)

            if text[0] == 'say' or text[0] == 'hello' or text[0] == 'hi':
                if 'hello' or 'hi' in text:
                    speak('Hello, my name is ' + activationWord + ' whats yours?')
                elif 'how are you' or 'how have you been' in text:
                    speak("I'm doing well, how about you?")
                else:
                    text.pop(0)
                    speech = ' '.join(text)
                    speak(speech)

            if text[0] == 'go' and text[1] == 'to':
                speak('Opening...')
                text = ' '.join(text[2:])
                webbrowser.get('chrome').open_new(text)

            if text[0] == 'wikipedia' or text[0] == 'search':
                text = (text[1])
                print(text)
                speak('Okay sure no problem bro I got you...')
                speak(search_wikipedia(text))