#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:29:09 2022

@author: vaibhav
"""

from assistant_function import *

# conversation starts from Here
speak("This is Vini , How can I help you")
speak("For interactive conversation please let me know your name")
naam = listen_Vini()
if naam == "~":
   speak("Couldn't understand your name. For my convinience I'll be calling you vaibhav")
   naam = "vaibhav"
outtext = " , Good to see you "
wish(naam + outtext)


while True:
    mytext = listen_Vini()
    # case to responds if it doesn't listen anything
    if mytext == "~":
        outtext = "Couldn't get you , Please say again"
        speak(outtext)
        
          

    # changing user name
    elif "change my name" in mytext or "change user" in mytext or "change name" in mytext:
        speak("For interactive conversation please let me know your new name")
        naam = listen_Vini()
        outtext = " , Good to see you "
        wish(naam + outtext)

    elif "open youtube" in mytext:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    # case that will stop the conversation
    elif "stop" in mytext or "exit" in mytext or "bye" in mytext or "go now" in mytext:
        outtext = "Ok " + naam + " , hope to see you again"
        speak(outtext)
        break
    
    
    #for interactive conversation     
    elif "thank you" in mytext or "thanks" in mytext or "thank u" in mytext:
         speak("It's my pleasure "+naam)

    # case that will wish you
    elif "hi" in mytext or "hello" in mytext:
        outtext = " , Good to see you "
        wish(naam + outtext)

    # case that will introduce itself
    elif "who are you" in mytext or "introduce yourself" in mytext or "what is your name" in mytext:
        outtext = "I am Vini !"
        speak(outtext)

    # case that will respond , when someone ask how are you or something like that
    elif "how are you" in mytext or "is all good" in mytext:
        outtext = "I am fine , what about you"
        speak(outtext)
        
    #sending email
    elif "send email" in mytext or "send mail" in mytext or "send a mail" in mytext or "send a email" in mytext:
        speak("Please type only mail id and nothing else")
        email_id=input("Enter email id only - ")
        speak("Please type message that need to be sent to " + email_id +" and nothing else")
        message=input("Enter message - ")
        speak(send_mail(email_id, message))
        
        
        
    #calculator
    elif "calculate" in mytext or "sum" in mytext or "some" in mytext  or "product" in mytext or "divide" in mytext or "add" in mytext or "addition" in mytext or "multiply" in mytext or "division" in mytext or "subtract" in mytext or "subtraction" in mytext or "difference" in mytext:
        out_cal=calculator(mytext)
        if "sum" in mytext or "some" in mytext  or "add" in mytext or "addition" in mytext :
            speak(addition(out_cal))
        elif "product" in mytext or "multiply" in mytext:
            speak(product(out_cal))
        elif "divide" in mytext or "division" in mytext:
            speak(division(out_cal))
        elif "subtract" in mytext or "subtraction" in mytext:
            speak(sub(out_cal))
        elif "difference" in mytext:
            speak(difference(out_cal))
        
        
    # this case will respond for interactive conversation
    elif "not fine" in mytext or "not well" in mytext:
        outtext = "So sad to hear that. Is there anything that I can do for you ?"
        speak(outtext)

    # this case will respond for interactive conversation
    elif "fine" in mytext or "well" in mytext:
        outtext = "It's good to know that you are fine"
        speak(outtext)

    # this case will respond when someone appreciate her
    elif "that's good" in mytext or "that's nice" in mytext:
        outtext = "Thank's for your compliment"
        speak(outtext)
        
        
    #this case will create txt file in the same directory
    elif "create a file" in mytext or "create file" in mytext:
        speak("What should be the file name ?")
        file_name=listen_Vini()
        if "~" in file_name:
            speak("Sorry "+naam+" couldn't able to create your file")
        else:
            file_name=create_file_name(file_name)
            speak("Please tell the the line's which need to be added in "+file_name)
            content=listen_Vini()
            if "~" in content:
                with open(file_name, 'x') as f:
                      f.write("")
                speak(file_name+" is created successfully . Please make a note that it is a empty file as I couldn't recognize any words that you speak . I highly apologize for this")
            else:
                with open(file_name, 'x') as f:
                      f.write(content)
                speak(file_name+" is created successfully")
            

    # this case will respond when someone ask about himself/herself
    elif "who am i" in mytext or "who i am" in mytext:
        outtext = "If you don't know than how should i know . But if you can talk then you may be human."
        speak(outtext)

    # this will reply current date
    elif "today's date" in mytext:
        today = date.today()
        d = today.strftime("%B %d, %Y")
        t = "Today is "
        outtext = t + d
        speak(outtext)

    # this will tell current week day
    elif "today's day" in mytext:
        today = date.today()
        d = calendar.day_name[today.weekday()]
        t = "Today is "
        outtext = t + d
        speak(outtext)

    # this case will some random technical jokes
    elif "joke" in mytext:
        speak(pyjokes.get_joke())

    # this case is for comedy
    elif "who is your boyfriend" in mytext or "you single" in mytext:
        outtext = "I am in relationship with vaibhav"
        speak(outtext)

    # this case will search anything in wikipedia and respond's accordingly
    elif "who is" in mytext in mytext:
        speak(
            "Please hold on "
            + naam
            + " , I am diving in Wikipedia , Therefore it will take some time !"
        )
        mytext = mytext.replace("wikipedia", "")
        try:
            results = wikipedia.summary(mytext, sentences=4)
            speak("According to Wikipedia \n" + results)
        except:
            speak("Sorry " + naam + " didn't find '" + mytext + "' in wikipedia")
    
    elif "what" in mytext or "how" in mytext or "when" in mytext or "why" in mytext:
        speak("I request "+naam+" to have patience coz I am still learning so I'll take some time to answer your question")
        out=search(mytext)
        if out=="~":
            speak("Sorry "+naam+" i am still learning so, I don't have the answer for your question right now.")
        else:
            speak(out)
    # this will pause Vini for some due course of time
    elif "hold" in mytext or "wait" in mytext or "pause" in mytext:
        more = "yes"
        f = 0
        while "yes" in more:
            if f == 0:
                speak("For how much time , should I wait ? ")
            a = listen_Vini()
            t = wait_time(a)
            if t == -1:
                outtext = "Couldn't get you , Please say again"
                speak(outtext)
                more = "yes"
                f = 1
            else:
                rt = return_time(a)
                speak("I'll get back to you in " + rt)
                time.sleep(t)
                befor_wake = 0
                if befor_wake == 0:
                    speak(rt + " is over " + naam + " , should i wait more ?")
                    more = listen_Vini()
                    f = 0
                else:
                    break
        speak("I hope you have completed that pending work")

    # if anything doesn't match then it will reply same as the question
    else:
        speak(mytext)









