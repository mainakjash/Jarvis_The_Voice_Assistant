import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning User !!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon User !!")

    elif hour>=18 and hour<21:
        speak("Good evening User !!")

    else:
        speak("Good night User !!")

    speak("Hi, Jarvis at your service. How may I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language = "en-in")
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)
        print("Please say that again..")
        return("None")

    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<sender_email>','<sender_email_password>')
    server.sendmail('<sender_email>',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com", new=2)

        elif "open google" in query:
            webbrowser.open("google.com", new=2)

        elif "play music" in query:
            music_dir = "C:\\Tito_Flash_Drive\\Desktop_backup\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open powerpoint" in query:
            apppath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(apppath)

        elif "send email to tito" in query:

            try:
                speak("What should I say, Sir?")
                content = takeCommand()
                to = "<recepient_email>"
                sendEmail(to,content)
                speak("Email has been sent..")

            except Exception as e:
                print(e)
                speak("Sorry Sir, could not send email..")