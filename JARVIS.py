#_____________________________________________________J.A.R.V.I.S________________________________________________________
#Python modules used for this programm
import sys
from turtle import speed
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import pyjokes
import webbrowser
import time
import os
import cv2

from requests import get
from requests.api import request
import smtplib
import psutil
import instaloader
import pyautogui
from PIL import ImageGrab
import numpy as np 
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from JarvisUi import Ui_JarvisUI
from state import state
from pywikihow import search_wikihow
import speedtest
from pytube import YouTube
import qrcode
from keyboard import press
from keyboard import write



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[4].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Main classs where all the functiona are present
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Intro()
    
    #function that will take the commands  to convert voice into text
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                query = listener.recognize_google(voice,language='en-in')
                query = query.lower()  
                if 'jarvis' in query: 
                    query = query.replace('jarvis','')
                
            return query
        except:
            return 'None'
        
    #Jarvis commands controller 
    def run_jarvis(self):
        self.wish()
        self.talk('Hello boss I am jarvis your assistant. please tell me how can i help you')
        while True:
            self.command = self.take_Command() #Every time taking command after a task is done
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) :

        #commands for opening youtube, playing a song in youtube, and download a song in youtube
                self.yt(self.command) 


            #Interaction commands with JARVIS
            elif ('your age' in self.command) or ('are you single'in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('i love you' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('hai' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('university name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command) or ('date' in self.command):
                self.Fun(self.command)


            #schedule commands for remembering you what is the plans of the day
            elif ("college time table" in self.command) or ("schedule" in self.command):
                self.shedule() 


            #It will tell the day 
            elif ("today" in self.command):
                day = self.Cal_day()
                self.talk("Today is "+day)
            
            
            #command if you don't want the JARVIS to speak until for a certain time
            elif ('silence' in self.command) or ('silent' in self.command) or ('keep quiet' in self.command) or ('wait' in self.command) :
                self.silenceTime(self.command)


            #Command for opening your social media accounts in webrowser 
            elif ('facebook' in self.command) or ('whatsapp' in self.command) or ('open my ' in self.command) or ('twitter' in self.command):
                self.social(self.command)



            #command for opening your OTT platform accounts

            elif ('hotstar' in self.command) or ('prime' in self.command) or ('netflix' in self.command):
                self.OTT(self.command)


            #Command for opening your online classes links
            elif ('online classes'in self.command):
                self.OnlineClass(self.command)


            #command for opeing college websites
            elif('mis'in self.command):
                self.college(self.command)


            #command to search for something in wikipedia
            elif ('wikipedia' in self.command) or ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command):
                self.B_S(self.command)


            #command for opening your browsers and search for information in google
            elif ('open google'in self.command) or ('open edge'in self.command) :
                self.browse(self.command)


            #command to open your google applications
            elif ('open gmail'in self.command) or('open maps'in self.command) or('open calender'in self.command) or('open documents'in self.command )or('open spredsheet'in self.command) or('open photos'in self.command) or('open drive'in self.command) or('open news' in self.command):
                self.Google_Apps(self.command)


            #command to open your open-source accounts
            
            elif ('open github'in self.command) :
                self.open_source(self.command)


            #Command to open desktop applications
            elif ('open calculator'in self.command) or ('open notepad'in self.command) or ('open paint'in self.command) or ('open online classes'in self.command) or ('open os'in self.command) or ('open d'in self.command) or ('open picture'in self.command) or ('open code'in self.command) or ('open avinash'in self.command) or ('open mayank'in self.command) or ('open ai'in self.command):
                self.OpenApp(self.command)


            #Command to close desktop applications
            elif ('close calculator'in self.command) or ('close notepad'in self.command) or ('close paint'in self.command) or ('close online classes'in self.command) or ('close os'in self.command) or ('close d'in self.command) or ('close picture'in self.command) or ('close code'in self.command) or ('close avinash'in self.command) or ('close mayank'in self.command) or ('close ai'in self.command) :
                self.CloseApp(self.command)



            #command for opening shopping websites 
            elif ('flipkart'in self.command) or ('amazon'in self.command) :
                self.shopping(self.command)


            #command for asking your current location
            elif ('where i am' in self.command) or ('where we are' in self.command):
                self.locaiton()

            #command for opening command prompt 
            elif ('command prompt'in self.command) :
                self.talk('Opening command prompt')
                os.system('start cmd')


            #Command for opening an instagram profile and downloading the profile pictures of the profile
            elif ('instagram profile' in self.command) or("profile on instagram" in self.command):
                self.Instagram_Pro()


            #Command for opening taking screenshot
            elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
                self.scshot()



            #command for searching for a procedure how to do something
            elif "activate mod" in self.command:
                self.How()


            #command for increaing the volume in the system
            elif ("volume up" in self.command) or ("increase volume" in self.command):
                pyautogui.press("volumeup")
                self.talk('volume increased')


            #command for decreaseing the volume in the system
            elif ("volume down" in self.command) or ("decrease volume" in self.command):
                pyautogui.press("volumedown")
                self.talk('volume decreased')


            #Command to mute the system sound
            elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
                pyautogui.press("volumemute")
                self.talk('volume muted')


            #command for opening your mobile camera the description for using this is in the README file
            elif ("open mobile cam" in self.command):
                self.Mobilecamera()



            #command for opening your webcamera
            elif ('webcam'in self.command) :
                self.webCam()


            #Command for creating a new contact
            elif("add contact" in self.command):
                self.AddContact()


            #Command for searching for a contact
            elif("number in contacts" in self.command):
                self.NameIntheContDataBase(self.command)


            #Command for displaying all contacts
            elif("display contacts" in self.command):
                self.Display()


            #Command for checking covid status in India
            elif ("covid" in self.command) or  ("corona" in self.command):
                self.talk("Boss which state covid 19 status do you want to check")
                s = self.take_Command()
                self.Covid(s)



        
            #command for playing a dowloaded mp3 song in which is present in your system
            elif 'music' in self.command:
                music_dir = 'C:\\Users\\avina\\Music\\Mastiiii' #change the song path directory if you have songs in other directory
                songs = os.listdir(music_dir)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))



            #command for knowing your system IP addres
            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                self.talk(f"your IP address is {ip}")


            #command for seading a whatsapp group and individual message
            elif ('send a message' in self.command):
                self.whatsapp(self.command)


            #command for sending an email
            elif 'send email' in self.command:
                self.verifyMail()


            #command for checking the temperature in surroundings
            elif "temperature" in self.command:
                self.temperature()


            #Command to generate the qr codes
            elif "create a qr code" in self.command:
                self.qrCodeGenerator()


            #command for checking internet speed
            elif "internet speed" in self.command:
                self.InternetSpeed()


            #command to make the jarvis sleep
            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay boss, I am going to sleep you can call me anytime.")
                break


            #command for waking the jarvis from sleep
            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("boss, I am not sleeping, I am in online, what can I do for u")


            #command for exiting jarvis from the program
            elif ("goodbye" in self.command) or ("get lost" in self.command):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()


            #command for knowing about your system condition
            elif ('system condition' in self.command) or ('condition of the system' in self.command):
                self.talk("checking the system condition")
                self.condition()



            #command for knowing the latest news
            elif ('tell me news' in self.command) or ("the news" in self.command) or ("todays news" in self.command):
                self.talk("Please wait boss, featching the latest news")
                self.news()


            #command for shutting down the system
            elif ('shutdown the system' in self.command) or ('down the system' in self.command) or ('shutdown' in self.command):
                self.talk("Boss shutting down the system in 10 seconds")
                time.sleep(5)
                os.system("shutdown /s /t 5")



            #command for restarting the system
            elif ('restart the system' in self.command) or ('restart' in self.command):
                self.talk("Boss restarting the system in 10 seconds")
                time.sleep(5)
                os.system("shutdown /r /t 5")



            #command for make the system sleep
            elif ('sleep the system' in self.command) or ('sleep ' in self.command) :
                self.talk("Boss the system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

           

            
    #Intro msg
    def Intro(self):
        while True:
            self.permission = self.take_Command()
            print(self.permission)
            if ("wake up" in self.permission) or ("get up" in self.permission)  or ("utho" in self.permission) or ("jago" in self.permission):
                self.run_jarvis()
            elif ("goodbye" in self.permission) or ("get lost" in self.permission):
                self.talk("Thanks for using me boss, have a good day")
                sys.exit()
                
    #Talk 
    def talk(self,text):
        engine.say(text)
        engine.runAndWait()

    #Wish
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
        if (hour>=0) and (hour <=12) and ('AM' in t):
            self.talk(f'Good morning boss, its {day} and the time is {t}')
        elif (hour >= 12) and (hour <= 16) and ('PM' in t):
            self.talk(f"good afternoon boss, its {day} and the time is {t}")
        else:
            self.talk(f"good evening boss, its {day} and the time is {t}")

    #Weather forecast
    def temperature(self):
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.talk(f"current {search} is {temp}")
    
   
     
      

    # Mobile camera
    def Mobilecamera(self):
        import urllib.request
        import numpy as np
        try:
            self.talk(f"Boss opening mobile camera")
            URL = "http://192.168.144.27:8080/shot.jpg" 
            while True:
                imag_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(imag_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    self.talk(f"Boss closing mobile camera")
                    break;
            cv2.destroyAllWindows()
        except Exception as e:
            print("Some error occured")



    #Web camera
    def webCam(self):    
        self.talk('Opening camera')
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('web camera',img)
            k = cv2.waitKey(50)
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

    

    #covid 
    def Covid(self,s):
        try:
            from covid_india import states
            details = states.getdata()
            if "check in" in s:
                s = s.replace("check in","").strip()
                print(s)
            elif "check" in s:
                s = s.replace("check","").strip()
                print(s)
            elif "tech" in s:
                s = s.replace("tech","").strip()
            s = state[s]
            ss = details[s]
            Total = ss["Total"]
            Active = ss["Active"]
            Cured = ss["Cured"]
            Death = ss["Death"]
            print(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            self.talk(f"Boss the total cases in {s} are {Total}, the number of active cases are {Active}, and {Cured} people cured, and {Death} people are death")
            time.sleep(5)
            self.talk("Boss do you want any information of other states")
            I = self.take_Command()
            print(I)
            if ("check" in I):
                self.Covid(I)
            elif("no" in I):
                self.talk("Okay boss stay home stay safe")
            else:
                self.talk("Okay boss stay home stay safe")
        except:
            self.talk("Boss some error occured, please try again")
            self.talk("Boss do you want any information of other states")
            I = self.take_Command()
            if("yes" in I):
                self.talk("boss, Which state covid status do u want to check")
                Sta = self.take_Command()
                self.Covid(Sta)
            elif("no" in I):
                self.talk("Okay boss stay home stay safe")
            else:
                self.talk("Okay boss stay home stay safe")



    #Whatsapp
    def whatsapp(self,command):
        try:
            command = command.replace('send a message to','')
            command = command.strip()
            name,numberID,F = self.SearchCont(command)
            if F:
                print(numberID)
                self.talk(f'Boss, what message do you want to send to {name}')
                message = self.take_Command()
                hour = int(datetime.datetime.now().hour)
                min = int(datetime.datetime.now().minute)
                print(hour,min)
                
                if "group" in command:
                    kit.sendwhatmsg_to_group(numberID,message,int(hour),int(min)+1)
                else:
                    kit.sendwhatmsg(numberID,message,int(hour),int(min)+1)

                    press('enter')
                self.talk("Boss message have been sent")
            if F==False:
                self.talk(f'Boss, the name not found in our data base, shall I add the contact')
                AddOrNot = self.take_Command()
                print(AddOrNot)
                if ("yes" in AddOrNot) or ("add" in AddOrNot) or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                    self.AddContact()
                elif("no" in AddOrNot):
                    self.talk('Ok Boss')
        except:
            print("Error occured, please try again")

    
    #Add contacts
    def AddContact(self):
        self.talk(f'Boss, Enter the contact details')
        name = input("Enter the name :").lower()
        number = input("Enter the number :")
        NumberFormat = f'"{name}":"+91{number}"'
        ContFile = open("Contacts.txt", "a") 
        ContFile.write(f"{NumberFormat}\n")
        ContFile.close()
        self.talk(f'Boss, Contact Saved Successfully')

    #Search Contact
    def SearchCont(self,name):
        with open("Contacts.txt","r") as ContactsFile:
            for line in ContactsFile:
                if name in line:
                    print("Name Match Found")
                    s = line.split("\"")
                    return s[1],s[3],True
        return 0,0,False
    
    #Display all contacts
    def Display(self):
        ContactsFile = open("Contacts.txt","r")
        count=0
        for line in ContactsFile:
            count+=1
        ContactsFile.close()
        ContactsFile = open("Contacts.txt","r")
        self.talk(f"Boss displaying the {count} contacts stored in our data base")    
        for line in ContactsFile:
            s = line.split("\"")
            print("Name: "+s[1])
            print("Number: "+s[3])
        ContactsFile.close()

    #search contact
    def NameIntheContDataBase(self,command):
        line = command
        line = line.split("number in contacts")[0]
        if("tell me" in line):
            name = line.split("tell me")[1]
            name = name.strip()
        else:
            name= line.strip()
        name,number,bo = self.SearchCont(name)
        if bo:
            print(f"Contact Match Found in our data base with {name} and the mboile number is {number}")
            self.talk(f"Boss Contact Match Found in our data base with {name} and the mboile number is {number}")
        else:
            self.talk("Boss the name not found in our data base, shall I add the contact")
            AddOrNot = self.take_Command()
            print(AddOrNot)
            if ("yes add it" in AddOrNot)or ("yeah" in AddOrNot) or ("yah" in AddOrNot):
                self.AddContact()
                self.talk(f'Boss, Contact Saved Successfully')
            elif("no" in AddOrNot) or ("don't add" in AddOrNot):
                self.talk('Ok Boss')

    #Internet speed
    def InternetSpeed(self):
        self.talk("Wait a few seconds boss, checking your internet speed")
        speed = speedtest.Speedtest()
        dl = speed.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = speed.upload()
        up = up/(1000000)
        print(dl,up)
        self.talk(f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")
        


    #Search for a process how to do
    def How(self):
        self.talk("How to do mode is is activated")
        while True:
            self.talk("Please tell me what you want to know")
            how = self.take_Command()
            try:
                if ("exit" in how) or("close" in how):
                    self.talk("Ok sir how to mode is closed")
                    break
                else:
                    max_result=1
                    how_to = search_wikihow(how,max_result)
                    assert len(how_to) == 1
                    how_to[0].print()
                    self.talk(how_to[0].summary)
            except Exception as e:
                self.talk("Sorry sir, I am not able to find this")


    #Communication commands
    def comum(self,command):
        print(command)
        if ('hi'in command) or('hai'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello boss what can I help for u")
        else :
            self.No_result_found()



    #Fun commands to interact with jarvis
    def Fun(self,command):
        print(command)
        if 'your name' in command:
            self.talk("My name is jarvis")
        elif 'my name' in command:
            self.talk("your name is Avinash")
        elif 'university name' in command:
            self.talk("you are studing in National institute of technology Agartala") 
        elif 'what can you do' in command:
            self.talk("I talk with you until you want to stop, I can say time, open your social media accounts,your open source accounts, open google browser,and I can also open your college websites, I can search for some thing in google and I can tell jokes")
        elif 'your age' in command:
            self.talk("I am very young that u")
        elif 'date' in command:
            self.talk('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'are you single' in command:
            self.talk('No, I am in a relationship with wifi')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Yes boss I am here')
        elif 'tell me something' in command:
            self.talk('boss, I don\'t have much to say, you only tell me someting i will give you the company')
        elif 'thank you' in command:
            self.talk('boss, I am here to help you..., your welcome')
        elif 'in your free time' in self.command:
            self.talk('boss, I will be listening to all your words')
        elif 'i love you' in command:
            self.talk('I love you too boss')
        elif 'can you hear me' in command:
            self.talk('Yes Boss, I can hear you')
        elif 'do you ever get tired' in command:
            self.talk('It would be impossible to tire of our conversation')
        else :
            self.No_result_found()


    #Social media accounts commands
    def social(self,command):
        print(command)
        if 'facebook' in command:
            self.talk('opening your facebook')
            webbrowser.open('https://www.facebook.com/')
        elif 'whatsapp' in command:
            self.talk('opening your whatsapp')
            webbrowser.open('https://web.whatsapp.com/')
        elif 'open my' in command:
            self.talk('opening your instagram')
            webbrowser.open('https://www.instagram.com/')
        elif 'twitter' in command:
            self.talk('opening your twitter')
            webbrowser.open('https://twitter.com/')
        
        else :
            self.No_result_found()
        

    #clock commands
    def Clock_time(self,command):
        print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)
    


    #calender day
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
        
        return day_of_the_week


    #shedule function for remembering todays plans
    def shedule(self):
        day = self.Cal_day().lower()
        self.talk("Boss today's shedule is")
        Week = {"monday" : "Boss from 9:00 to 9:50 you have Cultural class, from 10:00 to 11:50 you have mechanics class, from 12:00 to 2:00 you have brake, and today you have sensors lab from 2:00",
        "tuesday" : "Boss from 9:00 to 9:50 you have English class, from 10:00 to 10:50 you have break,from 11:00 to 12:50 you have ELectrical class, from 1:00 to 2:00 you have brake, and today you have biology lab from 2:00",
        "wednesday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Data structures class, from 11:00 to 11:50 you have mechanics class, from 12:00 to 12:50 you have cultural class, from 1:00 to 2:00 you have brake, and today you have Data structures lab from 2:00",
        "thrusday" : "Boss today you have a full day of classes from 9:00 to 10:50 you have Maths class, from 11:00 to 12:50 you have sensors class, from 1:00 to 2:00 you have brake, and today you have english lab from 2:00",
        "friday" : "Boss today you have a full day of classes from 9:00 to 9:50 you have Biology class, from 10:00 to 10:50 you have data structures class, from 11:00 to 12:50 you have Elements of computing class, from 1:00 to 2:00 you have brake, and today you have Electronics lab from 2:00",
        "saturday" : "Boss today you have a full day of classes from 9:00 to 11:50 you have maths lab, from 12:00 to 12:50 you have english class, from 1:00 to 2:00 you have brake, and today you have elements of computing lab from 2:00",
        "sunday":"Boss today is holiday but we can't say anything when they will bomb with any assisgnments"}
        if day in Week.keys():
            self.talk(Week[day])



    #college resources commands
    def college(self,command):
        print(command)
        if 'mis' in command:
            self.talk('opening your MIS Account')
            webbrowser.open('https://mis.nita.ac.in/')
       
    
    #Online classes
    def OnlineClasses(self,command):
        print(command)
        if 'online class' in command:
            self.talk('opening your microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')



    #Brower Search commands
    def B_S(self,command):
        print(command)
        try:
            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who the heck is' in command):
                target1 = command.replace("who the heck is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("according to wikipedia "+info)
        except :
            self.No_result_found()
        


    #Browser
    def browse(self,command):
        print(command)
        if 'google' in command:
            self.talk("Boss, what should I search on google..")
            S = self.take_Command()   #taking command for what to search in google
            webbrowser.open(f"{S}")
        elif 'edge' in command:
            self.talk('opening your Miscrosoft edge')
            os.startfile('..\\..\\MicrosoftEdge.exe')   #path for your edge browser application
        else :
            self.No_result_found()



    #google applications selection
    def Google_Apps(self,command):
        print(command)
        if 'gmail' in command:
            self.talk('opening your google gmail')
            webbrowser.open('https://mail.google.com/mail/')
        elif 'maps' in command:
            self.talk('opening google maps')
            webbrowser.open('https://www.google.co.in/maps/')
        elif 'news' in command:
            self.talk('opening google news')
            webbrowser.open('https://news.google.com/')
        elif 'calender' in command:
            self.talk('opening google calender')
            webbrowser.open('https://calendar.google.com/calendar/')
        elif 'photos' in command:
            self.talk('opening your google photos')
            webbrowser.open('https://photos.google.com/')
        elif 'documents' in command:
            self.talk('opening your google documents')
            webbrowser.open('https://docs.google.com/document/')
        elif 'spreadsheet' in command:
            self.talk('opening your google spreadsheet')
            webbrowser.open('https://docs.google.com/spreadsheets/')
        else :
            self.No_result_found()
            


    #youtube
    def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk("Boss can you please say the name of the song")
            song = self.take_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk("Boss please enter the youtube video link which you want to download")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f"Boss downloaded {yt.title} from the link you given into the main folder")
        elif 'youtube' in command:
            self.talk('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()



    #Opensource accounts
    def open_source(self,command):
        print(command)
        if 'github' in command:
            self.talk('opening your github')
            webbrowser.open('https://github.com/MayAvi420')
        

    #OTT 
    def OTT(self,command):
        print(command)
        if 'hotstar' in command:
            self.talk('opening your disney plus hotstar')
            webbrowser.open('https://www.hotstar.com/in')
        elif 'prime' in command:
            self.talk('opening your amazon prime videos')
            webbrowser.open('https://www.primevideo.com/')
        elif 'netflix' in command:
            self.talk('opening Netflix videos')
            webbrowser.open('https://www.netflix.com/')
        else :
            self.No_result_found()


    #PC allications
    def OpenApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in command) :
            self.talk('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('notepad'in command) :
            self.talk('Opening notepad')
            os.startfile('c:\\Windows\\System32\\notepad.exe')
        elif ('os'in command) :
            self.talk('Opening OS(C) directory')
            os.startfile('C:\\')
        elif ('d'in command) :
            self.talk('Opening DATA(D) directory')
            os.startfile('D:\\')
        elif ('code'in command) :
            self.talk('Opening your Visual studio code')
            os.startfile('C:\\Users\\avina\\Desktop\\Visual Studio Code.lnk')
        elif ('online classes'in command) :
            self.talk('Opening your Microsoft teams')
            webbrowser.open('https://teams.microsoft.com/')
        elif ('avinash'in command) :
            self.talk('Opening collection of Hollywood movies and webseries file')
            os.startfile('D:\\Avinash')
        elif ('pic'in command) :
            self.talk('Opening college memories pictures')
            os.startfile("D:\\Picture\\Aaaaaa")
        elif ('mayank'in command) :
            self.talk('Opening collection of bollywood and tollywood movies')
            os.startfile("D:\\Captures")
        elif ('ai'in command) :
            self.talk('Opening AI folder')
            os.startfile("C:\\Users\\avina\\Desktop\\AI Program")
        
        else :
            self.No_result_found()



    #close applications function
    def CloseApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk("okay boss, closing caliculator")
            os.system("taskkill /f /im calculator.exe")
        elif ('paint'in command) :
            self.talk("okay boss, closing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('notepad'in command) :
            self.talk("okay boss, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('code'in command) :
            self.talk("okay boss, closing vs code")
            os.system("taskkill /f /im Visual Studio Code.lnk")
        elif ('online classes'in command) :
            self.talk("okay boss, closing online classes")
            os.system("taskkill /f /im teams.microsoft.com")
        elif ('avinash'in command) :
            self.talk("okay boss, closing folder")
            os.system("taskkill /f /im Avinash")
        elif ('mayank'in command) :
            self.talk("okay boss, closing this folder")
            os.system("taskkill /f /im Captures")
        elif ('pic'in command) :
            self.talk("okay boss, closing image gallery")
            os.system("taskkill /f /im Aaaaaa")
        elif ('ai'in command) :
            self.talk("okay boss, closing AI folder")
            os.system("taskkill /f /im AI Program")
        else :
            self.No_result_found()



    #Shopping links
    def shopping(self,command):
        print(command)
        if 'flipkart' in command:
            self.talk('Opening flipkart online shopping website')
            webbrowser.open("https://www.flipkart.com/")
        elif 'amazon' in command:
            self.talk('Opening amazon online shopping website')
            webbrowser.open("https://www.amazon.in/")
        else :
            self.No_result_found()



    #Time caliculating algorithm
    def silenceTime(self,command):
        print(command)
        x=0
        #caliculating the given time to seconds from the speech commnd string
        if ('10' in command) or ('ten' in command):x=600
        elif '1' in command or ('one' in command):x=60
        elif '2' in command or ('two' in command):x=120
        elif '3' in command or ('three' in command):x=180
        elif '4' in command or ('four' in command):x=240
        elif '5' in command or ('five' in command):x=300
        elif '6' in command or ('six' in command):x=360
        elif '7' in command or ('seven' in command):x=420
        elif '8' in command or ('eight' in command):x=480
        elif '9' in command or ('nine' in command):x=540
        self.silence(x)
        


    #Silence
    def silence(self,k):
        t = k
        s = "Ok boss I will be silent for "+str(t/60)+" minutes"
        self.talk(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.talk("Boss "+str(k/60)+" minutes over")


    #Mail verification
    def verifyMail(self):
        try:
            self.talk("what should I say?")
            content = self.take_Command()
            self.talk("To whom do u want to send the email?")
            to = self.take_Command()
            self.SendEmail(to,content)
            self.talk("Email has been sent to "+str(to))
        except Exception as e:
            print(e)
            self.talk("Sorry sir I am not not able to send this email")
    
    #Email Sender
    def SendEmail(self,to,content):
        print(content)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login("avinashmayank1372001@gmail.com","Avinash@13072001")
        server.sendmail("avinashmayank1372001@gmail.com",to,content)
        server.close()

    #location
    def locaiton(self):
        self.talk("Wait boss, let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f"Boss i am not sure, but i think we are in {city} city of {state} state of {country} country")
            self.talk(f"and boss, we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry boss, due to network issue i am not able to find where we are.")
            pass

    #Instagram profile
    def Instagram_Pro(self):
        self.talk("Boss please enter the user name of Instagram: ")
        name = input("Enter username here: ")
        webbrowser.open(f"www.instagram.com/{name}")
        time.sleep(5)
        self.talk("Boss would you like to download the profile picture of this account.")
        cond = self.take_Command()
        
        if('download' in cond) or ('ok' in cond):
            mod = instaloader.Instaloader()
            mod.download_profile(name,profile_pic_only=True)
            self.talk("I am done boss, profile picture is saved in your main folder. ")
        else:
            pass

    #ScreenShot
    def scshot(self):
        self.talk("Boss, please tell me the name for this screenshot file")
        name = self.take_Command()
        self.talk("Please boss hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.talk("I am done boss, the screenshot is saved in main folder.")

    #News
    def news(self):
        MAIN_URL_= " https://newsapi.org/v2/top-headlines?country=in&apiKey=370b2f61df874ae0bc260355a9f61e84"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            self.talk(f"todays {seq[i]} news is: {headings[i]}")
        self.talk("Boss I am done, I have read most of the latest news")


    #System condition
    def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battery = psutil.sensors_battery()
        percentage = battery.percent
        self.talk(f"Boss our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f"Boss we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f"Boss we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f"Boss we don't have enough power to work, please connect to charging")
        else:
            self.talk(f"Boss we have very low power, please connect to charging otherwise the system will shutdown very soon")



    #no result found
    def No_result_found(self):
        self.talk('Boss I couldn\'t understand, could you please say it again.')        



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
sys.exit(app.exec_())
