import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import pyjokes
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisGUI import Ui_JarvisGUI

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis tell me how can i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikaskum0ar@gmail.com', 'vikas12345@')
    server.sendmail('your mail id', to, content)
    server.close()

class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()
    
    def run(self):
        self.taskExecution()
        
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening......")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio)
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please.....")
            return "none"
        return query
    
    def taskExecution(self):
    # speak("hii hello")
        wish()
        while True:
            self.query = self.takecommand().lower()

            if "open chrome" in self.query:
                cr = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
                os.startfile(cr)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()
            elif "play music" in self.query:
                music_dir = "E:\\songs"
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("according to wikipedia...")
                speak(results)
                print(results)

            elif "news" in self.query:
                from NewsRead import latestNews
                latestNews()

            elif "open youtube" in self.query:
                speak("opening youtube")
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                speak("opening facebook")
                webbrowser.open("www.facebook.com")

            elif "open linkedin" in self.query:
                speak("opening linkedin")
                webbrowser.open("www.linkedin.com")

            elif "open google" in self.query:
                speak("sir what do I search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "send whatsapp message" in self.query:
                kit.sendwhatmsg("+916204042821", "kyaa re bhikmangya", 20, 13)

            elif "search songs on youtube" in self.query:
                kit.playonyt("see you again")

            elif "send email to vikas" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    to = "vikaskum1ar@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry sir i am not able to send this email")

            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day")
                sys.exit()
            elif "stop" in self.query:
                speak("ok sir")
                sys.exit()

            elif "close chrome" in self.query:
                speak("closing chrome sir")
                os.system("taskkill /f /im chrome.exe")

            elif "set alarm" in self.query:
                nn = int(datetime.datetime.now().hour)
                if nn == 00:
                    speak(f"alarm is set at {nn}")
                    music_dir = "E:\\songs"
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[1]))

            elif "tell me a joke" in self.query:
                jk = pyjokes.get_joke()
                speak(jk)

            elif "shut down the system" in self.query:
                os.system('shutdown /s /t 5')
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep the system" in self.query:
                os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")

            speak("sir, do you have any other work")

startExecution = MainThread()

class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Gifs/MImN.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Gifs/7kmF.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Gifs/SUV4.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Gifs/Jarvis_Loading_Screen.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Gifs/7fi4")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        time = current_time.toString("hh:mm:ss")
        date = current_date.toString("dd/MM/yyyy")
        self.ui.textBrowser.setText("\n\nDate: "+date+"\n\nTime: "+time)

app = QApplication(sys.argv)
jarvis = UserInterface()
jarvis.show()
exit(app.exec_())