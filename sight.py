import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_action():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            action = listener.recognize_google(voice)
            action = action.lower()
            if 'alexa' in action:
                action = action.replace('alexa', '')
                print(action)
    except:
        pass
    return action


def run_alexa():
    action = take_action()
    print(action)
    if 'play' in action:
        song = action.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in action:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif 'who the heck is' in action:
        person = action.replace('Tell me about', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'who are you' in action:
        talk('Im Sight, your human dating assistant!')
    elif 'date' in action:
        talk('404: Intention to date not found.')
    elif 'are you single' in action:
        talk('Sorry, my relationship variable is stored as a double.')
    elif 'joke' in action:
        talk(pyjokes.get_joke())
    elif '' in action:
        talk(pyjokes.get_joke())
        talk ('Did you say ' + action + "?")
    else:
        talk ('Please say the action again - or tell me what you think; I can help you practice!')
    


while True:
    run_alexa()