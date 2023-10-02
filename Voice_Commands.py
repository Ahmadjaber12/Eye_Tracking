import pyttsx3
import speech_recognition as sr
import pyautogui
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os  
import time



engine = pyttsx3.init()# for convering text to voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
      
     r = sr.Recognizer()
      
     with sr.Microphone() as source:#use the microphone as input
          
         print("Listening...")
         r.pause_threshold = .5 
         audio = r.listen(source)#for listenning to the user
         global query
     try:
         print("Recognizing...")   
         query = r.recognize_google(audio, language ='en-in')#analyzing the voice in google 
         print(f"User said: {query}\n")
   
     except Exception as e:
         print(e)   
         print("Unable to Recognize your voice.") 
         takeCommand()
     return query
if __name__=='__main__':
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                   speak('Searching Wikipedia...')
                   query = query.replace("wikipedia", "")
                   results = wikipedia.summary(query, sentences = 3)
                   speak("According to Wikipedia")
                   print(results)
                   speak(results)   
            elif 'youtube' in query:
                   speak("Here you go to Youtube\n")
                   webbrowser.open("youtube.com")
            elif 'right' in query:
                   pyautogui.keyUp('alt') 
                   speak("what do you want to write?\n")
                   text=takeCommand().lower()
                   pyautogui.write(text+" ")
            elif 'google' in query:
                   speak("Here you go to Google\n")
                   webbrowser.open("google.com")
            elif 'facebook' in query:
                   speak("Here you go to your facebook ")
                   webbrowser.open("facebook.com")
            elif 'double' in query:
                pyautogui.click()
                pyautogui.click()
            elif 'click' in query:
                pyautogui.leftClick()
            elif 'left' or 'lift' in query:
                pyautogui.rightClick()
            elif 'close' in query:
                pyautogui.hotkey('alt','f4')    
            elif 'switch' in query:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')
            else: 
                speak("didn't hear you")
            
                   
                   
            
