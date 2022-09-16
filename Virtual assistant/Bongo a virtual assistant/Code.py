import audioop #The audioop module contains some useful operations on sound fragments.
import ctypes #ctypes is a foreign function library for Python.
import shutil #Python’s shutil module provides us a number of high-level operations on files.
import subprocess #Subprocess in Python is a module used to run new codes and applications by creating new processes
import time 
from tkinter.colorchooser import askcolor #Tkinter is a graphical user interface module for Python. Tkinter provides colorchooser module using which color toolbox can be displayed
from tkinter.filedialog import askdirectory 
import pyttsx3 #pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as sr
import datetime
import os 
import webbrowser
import pyjokes
from time import ctime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
    
def there_exists(terms):
        for term in terms:
            return True

        
r = sr.Recognizer() 
def record_audio(ask=False):        
        
    with sr.Microphone() as source: 
        r.energy_threshold=500            
        r.adjust_for_ambient_noise(source,1.2)
        r.pause_threshold= 1
        if askcolor:
            speak(askdirectory)
        
        voice_data = ''       

    try :
            voice_data = r.recognize_google(audioop)
       
    except sr.RequestError:
            speak('Sorry, the service is down')
    except sr.UnknownValueError: 
            print('Recognizing..')
    print(f">> {voice_data.lower()}") 
    return voice_data.lower()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def run_bongo():
        
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname =("This is Bongo")
    speak("I am your Assistant")
    speak(assname)
    
def username():
    speak("What should i call you sir")
    Gentleman = takeCommand()
    speak("Welcome Mister")
    speak(Gentleman)
    columns = shutil.get_terminal_size().columns
    
    print("******************************************".center(columns))
    print("Welcome Mr.",Gentleman.center(columns))
    print("******************************************".center(columns))
    
    speak("How can i Help you, Sir")

def takeCommand():

    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "Gentleman"
    
    return query

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    run_bongo()
    username()
    
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


    

while True:
             
        query = takeCommand().lower()
                  
        if 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
                continue 
            
        elif 'hello' in query:
               speak("wow, that's the most amazing thing i heard today")
               continue
            
        elif 'bongo' in query:           
            run_bongo()
            speak("bongos 1 point o in your service Mister")
            continue
            

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop bongo from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a) 
            continue

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
            continue
 
        elif 'open stack overflow' in query:
            speak("Here you go to stackoverflow")
            webbrowser.open("stackoverflow.com")
            continue
            
        elif 'open facebook' in query:
            speak("Here you go to facebook")
            webbrowser.open("facebook.com")
            continue
            
        elif 'open danish college' in query:
            speak("Here you go to dhaanish college")
            webbrowser.open("https://www.dhaanish.in")
            continue
            
        elif 'open anna university' in query:
            speak("Here you go to anna university")
            webbrowser.open("https://www.annauniv.edu") 
            continue          
 
        elif 'my location' in query:
            speak("here you go to your location")
            webbrowser.open("https://google.nl/maps/place/")
            continue
            
        elif 'open google' in query:
            speak("Here you go to google")
            webbrowser.open("https://www.google.com/")
            continue
 
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f') 
            continue
        
        elif "which day it is" in query:
            tellDay()
            continue
                     
        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke()) 
            continue
                      
        elif 'who are you' in query:
           speak("i am bongo your voice assistent sir !")
           continue
          
        elif 'what is your name' in query:
          speak("i am bongo your voice assistent sir !")
          continue
          
        elif 'who am i' in query:
          speak("If you talk then definitely your human")
          continue
          
        elif 'why i came to world' in query:
          speak("Thanks to god. further It's a secret") 
          continue
        
        elif 'how are you' in query:
          speak("I'm fine, nice to meet you")
          continue
          
        elif 'i love you' in query:
            speak("sorry, It's hard to understand")
            continue
        
        elif 'i like you' in query:
            speak("I am sorry, but I Do not think of you that way")
            continue
        
        elif 'open wikipedia' in query:
            speak("here we go to wikipedia")
            webbrowser.open("wikipedia.com")
            continue
                
        elif 'are you single' in query:
            speak("no im comitted to my developer")
            continue
            
        elif 'thank you' in query:
            speak("welcome")  
            continue           
            
        elif 'who is the prime minister of india' in query:
            speak("Narendra Modi") 
            continue                  
        
        elif 'time' in query:
            speak(ctime())  
            continue
            
        elif 'tell about' in query:
            speak("Checking the wikipedia ")
            query = query.replace('tell about', '')
            info = wikipedia.summary(query, 4)
            speak("According to wikipedia")
            speak(info)
            continue
        
        elif 'who is' in query:
            speak("Checking the wikipedia ")
            query = query.replace('who is', '')
            info = wikipedia.summary(query, 4)
            speak("According to wikipedia")
            speak(info)
            continue
        
        elif "bye" in query:
            speak("we started with a hello but ended with a comlicated goodbye")
         
         
        elif 'search' in query:
            speak("Checking the google ")
            query = query.replace('search', '')
            link = f"https://www.google.com/search?q={query}"
            webbrowser.open(link)
           
    
    
        
        
        
        
