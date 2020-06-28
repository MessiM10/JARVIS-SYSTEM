import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is ")
    speak(Time)

def date():
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    speak("The current day is ")
    speak(year)
    speak(month)
    speak(day)

def wishMe():
    speak("Welcome back Sir")
    time()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning Mr Jha")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon Mr Jha")
    elif hour >= 16 and hour < 20:
        speak("Good Evening Mr Jha")
    else:
        speak("Good Nighr Mr Jha")

    date()
    speak("Jarvis At Your Service.. How can I Help You Jha??")

# wishMe()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Say that thing again Please...")
        return "None"

    return query

def sendMail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('ankitrck6@gmail.com','Rambaan@10')
    server.sendmail('ankitrck6@gmail.com',to,content)
    server.close()

def Screenshot():
    img=pyautogui.screenshot()
    img.save('/Users/avinashsinghranawat/Desktop\\ss.png')

def Cpu():
    usuage=str(psutil.cpu_percent())
    speak("CPU IS AT "+usuage)
    battery=str(psutil.sensors_battery())
    speak("Battery is at ")
    speak(battery.percent)

def Jokes():
    print(pyjokes.get_joke())
    speak(pyjokes.get_joke())

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()



        elif 'wikipedia' in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say??")
                content=takeCommand()
                to=takeCommand()
                sendMail(to,content)
                speak("Email is sent")

            except Exception as e:
                print(e)
                speak("Unable to send the email")


        elif 'open google' in query:
            speak("What should i search for??")
            chromepath='/Users/avinashsinghranawat/Library/Application Support/Google/Chrome/Profile 3'
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'logout' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'remeber' in query:
            speak("What should i remember??")
            data=takeCommand()
            speak("You said me to remember "+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember=open('data.txt','r')
            speak("you said me to remember that"+remember.read())

        elif 'screenshot' in query:
            Screenshot()
            speak("Successfully taken the screenshot")

        elif 'cpu' in query:
            Cpu()

        elif 'joke' in query:
            Jokes()


        elif 'offline' in query:
            quit()


