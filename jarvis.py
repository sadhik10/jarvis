import pyttsx3
import speech_recognition as sr
import datetime
import os 
import wikipedia 
import webbrowser
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voices',voices[1].id)
#print(voices[1])
engine.setProperty("rate",175)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source,timeout=2,phrase_time_limit=5)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"you said:{query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<=18:
        speak("good afternoon..!")
    else:
        speak("good eveing")
    speak("this is jarvis sir,please tell me how can i help you")
if __name__== "__main__":
    wish()
    while True:
        query=takecommand().lower()
        if "open wordpad" in query:
            # path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.exe"
            path="C:\Program Files\Microsoft Office\\root\Office16\WINWORD.EXE"    
            os.startfile(path)
        elif "open notepad" in query:
            path="C:\Windows\System32\\notepad.exe"
            os.startfile(path)
        elif "open powerpoint" in query:
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\powerpoint.exe"
            os.startfile(path)
        # search wikipedia
        elif "wikipedia" in query:
            search=query.replace("wikipedia","")
            results=wikipedia.summary(search,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open androidstudio" in query:
            path="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Program"
            os.startfile(path)
        #search chrome
        elif "open chrome" in query:
            path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(path)
        elif "open excel" in query:
            path="C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(path)
            sleak("opening excel sir")
        elif "open taskbar" in query:
            path="C:\Program Files\Microsoft"
            os.startfile(path)
        elif "open calender" in query:
            path="C:\Program Files\Microsoft"
            os.startfile(path)
        elif "open filemanger" in query:
            path="C:\Program Files\Microsoft"
            os.startfile(path)
        elif "in whatsup" in query:
            search=query.replace("in whatsup", "")
            search=search.replace("search", "")
            url = (f"https://api.whatsapp.com/send?phone={search}")
            webbrowser.open(url)
        elif "in instagram" in query:
            search=query.replace("in instagram","")
            s
    # stop loop
        elif "exit" in query:
            break 
        #search something from chrome
        
        elif "in google" in query:
            search=query.replace("in google","")
            search=query.replace("search","")
            url = (f"https://www.google.com/search?q={search}")
            webbrowser.open(url)
        elif "in youtube" in query:
            search=query.replace("in youtube","")
            search=query.replace("search","")
            url = (f"https://www.youtube.com/results?search_query={search}")
            webbrowser.open(url)
        elif "in facebook" in query:
            search=query.replace("in facebook","")
            search=query.replace("search","")
            url = (f"https://www.facebook.com/search/top/?q={search}")
            webbrowser.open(url)
        #shutdwon system
        elif "shutdown" in query:
            os.system(shutdown)
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "log off" in query:
            os.system("shutdown /l /t 1") 
        
            
    #speak("this is jarvis, how can i help you")