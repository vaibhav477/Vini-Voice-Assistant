#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:21:09 2022

@author: vaibhav
"""

# important library
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import datetime
import calendar
from datetime import date
import pyjokes
import wikipedia
import time
import webbrowser
import os
import requests
import re
import bs4
import html2text
import smtplib 
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# Language for whole conversation
language = "en-in"


# function that is listenting user's voice
def listen_Vini():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)

        print("Listening your voice.......")

        # capture the audio
        audio = r.listen(source)

    try:
        mytext = r.recognize_google(audio)
        mytext = mytext.lower()
        return mytext
    except:
        return "~"
    
    
    
    
# Function which will respond for google search related query   
def dataFetchURL(url):
    
    data=requests.get(url)
    
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    
    txt=soup.get_text()    
    content = html2text.html2text(txt)
    
    return content

model_name = "deepset/roberta-base-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

def QA(text,qtxt):
    QA_input = {
        'question': qtxt,
        'context': text
    }
    res = nlp(QA_input)

    # b) Load model & tokenizer
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    return res




# function that will wakeup the Vini before its time  voice
def wake_Vini():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        # clear background noise
        r.adjust_for_ambient_noise(source, duration=0.3)

        # capture the audio
        audio = r.listen(source)

    try:
        mytext = r.recognize_google(audio)
        mytext = mytext.lower()
        return mytext
    except:
        return "~"


# function that will say the answer which is recieved
def speak(outtext):
    myobj = gTTS(text=outtext, lang=language, slow=False)
    myobj.save("temp.mp3")
    print("Vini : ", outtext)
    playsound("temp.mp3")


# function to wish according to time
def wish(outtext):
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        outtext = "Good Morning " + outtext
        speak(outtext)

    elif hour >= 12 and hour < 18:
        outtext = "Good Afternoon " + outtext
        speak(outtext)

    else:
        outtext = "Good Evening " + outtext
        speak(outtext)


# function that will convert time
def wait_time(a):

    # this will calculate the number
    i = 0
    l = len(a)
    f = 0
    for char in a:
        if char.isdigit():
            t = a[i]
            i += 1
            while i < l and a[i] >= "0" and a[i] <= "9":
                t = t + a[i]
                i += 1
            ti = int(t)
            f = 1
            break
        else:
            i += 1
    if f == 0:
        return -1

    # this will find the format i.e hour/sec/minute
    if "hour" in a:
        ti = ti * 60 * 60
    elif "minute" in a:
        ti = ti * 60
    elif "second" in a:
        ti = ti * 1
    else:
        return -1

    return ti


def return_time(a):

    # this will calculate the number
    i = 0
    l = len(a)
    for char in a:
        if char.isdigit():
            t = a[i]
            i += 1
            while i < l and a[i] >= "0" and a[i] <= "9":
                t = t + a[i]
                i += 1
            break
        else:
            i += 1

    # this will find the format i.e hour/sec/minute
    if "hour" in a:
        if t == 1:
            t = "a hour"
        else:
            t = t + " hours"
    elif "minute" in a:
        if t == 1:
            t = "a minute"
        else:
            t = t + " minutes"
    elif "second" in a:
        if t == 1:
            t = t + " second"
        else:
            t = t + " seconds"

    return t




#function to create the name of file
def create_file_name(s):
    out=""
    if 'dot' in s:
        s.split(' dot')
        out=s.split(' dot')[0]+".txt"
    else:
        s.split('.')
        out=s.split('.')[0]+".txt"
    return out



# calculator
def calculator(a):
    i = 0
    l = len(a)
    out_arr=[]
    while i < l:
        if a[i].isdigit() and i<l :
            t = a[i]
            i += 1
            while i < l and a[i] >= "0" and a[i] <= "9":
                t = t + a[i]
                i += 1
            if t!=' ':
                inse=int(t)
                out_arr.append(int(inse))
        i+=1
            
    return out_arr



def addition(out_arr):
    if len(out_arr)>1:
        return(str(abs(out_arr[0]+out_arr[1])))
    else :
        return ("Sorry couldn't able to calculate")



def difference(out_arr):
    if len(out_arr)>1:
        return(str(abs(out_arr[0]-out_arr[1])))
    else :
        return ("Sorry couldn't able to calculate")




def product(out_arr):
    if len(out_arr)==0:
        return 0
    result = 1
    for x in out_arr:
         result = result * x
    return (str(result))




def division(out_arr):
    if len(out_arr)>1:
        return(str(abs(out_arr[0]/out_arr[1])))
    else :
        return ("Sorry couldn't able to calculate")




def sub(out_arr):
    if len(out_arr)>1:
        return (str(out_arr[1]-out_arr[0]))
    else :
        return ("Sorry couldn't able to calculate")





# google search
def search(question):
    try:
        from googlesearch import search
    except ImportError:
        return ("No module named 'google' found") 
    
    for j in search(question, tld="co.in", num=1, stop=1, pause=1):
        try:
            result=dataFetchURL(j)
            if "wikipedia" in result:
                question = question.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(question, sentences=4)
                    return("According to Wikipedia \n" + results)
                except:
                    return ("~" ) 
            else:
                output=QA(result,question)
                try:
                   return (output['answer'])
                except:
                   return ("couldn't find any thing")
        except:
            return ("couldn't find any thing")
        
        
        
        
#sending email
#don't forget to turn of 2-step verification from your mail
def send_mail(email_id,message):
    try: 
        #Create your SMTP session 
        smtp = smtplib.SMTP('smtp.gmail.com', 587) 

        #Use TLS to add security 
        smtp.starttls() 

        #User Authentication 
        smtp.login("sender's email id","sender' email password")

        #Sending the Email
        smtp.sendmail("sender's email id", email_id,message) 

        #Terminating the session 
        smtp.quit() 
        return ("Email sent successfully!") 

    except Exception as ex: 
        return("Something went wrong...." + str(ex))



    
