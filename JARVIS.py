import speech_recognition as sr
from time import sleep
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    with sr.Microphone() as source:
        listner.adjust_for_ambient_noise(source)
        voice = listner.listen(source)
        try:
            command = listner.recognize_google(voice)
            command = command.lower()
        except sr.RequestError:
            talk("Sorry, the I can't access the Google API...")
        except sr.UnknownValueError:
            talk("Sorry, Unable to recognize your speech...")
    return command


def run_jarvis_command(command):
    if "name" in command:
        talk("I am JARVIS")

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("The Time is : ", time)
        talk('Current Time is ' + time)

    if "search" in command:
        talk("What do you want me to search for?")
        keyword = take_command()
        # if "keyword" is not empty
        if keyword != '':
            url = "https://google.com/search?q=" + keyword
            # webbrowser module to work with the webbrowser
            talk("Here are the search results for " + keyword)
            webbrowser.open(url)
            sleep(3)

    if "quit" in command or "exit" in command:
        talk("Ok, I am going to take a nap...")
        exit()

    else:
        talk("Sorry, I am working on that command..")


sleep(1)
while True:
    talk("Listning...")
    print("listning...")
    command = take_command()
    run_jarvis_command(command)
