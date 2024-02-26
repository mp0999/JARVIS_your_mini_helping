import pyttsx3                                    #pip install pyttsx3
import speech_recognition as sr                   #pip install speechRecognition
import pyaudio
import datetime
import wikipedia                                  #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis sir. Please tell me how may i help you!")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)    
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("your_@email_id", "Password")
    server.sendmail('your_@email_id', to, content)
    server.close()
    
if __name__ == "__main__":
    speak("Radhe radhe jay shree krishna radhe radhe")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        
        # Logic for excuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open_new_tab("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
            
        
        elif 'play music' in query:
            music_dir = "C:\\Users\\mayur\\Music"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"gentelman, The time is {strTime}")
            
        elif 'open code' in query:
            path = "C:\\Users\\mayur\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'sent email to mp' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "your_@email_id"
                sendEmail(to, content)
                speak("Your email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend emailwada bhai. i am not able to sent this email")
                
        # elif "any" in query:
        #     pass
        
        
