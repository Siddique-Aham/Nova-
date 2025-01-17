import os
from os import startfile
from pyautogui import click
from keyboard import press, press_and_release, write
import pyttsx3
import speech_recognition as sr
import webbrowser as web
import speedtest
import pywhatkit
import wikipedia  # For Wikipedia search
import requests # For making API requests
import time  # For handling delays

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set to female voice

# Speak function to output audio
def Speak(audio):
    try:
        print(f": {audio}")
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in Speak function: {e}")

# Function to take voice command from microphone
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": Your Command: {query}\n")
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return query.lower()

# Function to take text input
def PromptCommand():
    command = input("Enter your command: ")
    return command.lower()

# Function to pause/play the YouTube video
def YouTubePausePlay():
    try:
        press('space')  # Space key toggles pause/play on YouTube
        Speak("Video paused or resumed.")
    except Exception as e:
        print(f"Error: {e}")
        Speak("Unable to pause or resume the video.")
        # Function to play YouTube video directly
def YouTubePlay(video):
    try:
        Speak(f"Playing {video} on YouTube.")
        pywhatkit.playonyt(video)
    except Exception as e:
        print(f"Error: {e}")
        Speak("Unable to play the video on YouTube.")


# Function to skip forward 10 seconds
def YouTubeSkipForward():
    try:
        press('right')  # Right arrow key skips forward 10 seconds
        Speak("Skipped forward 10 seconds.")
    except Exception as e:
        print(f"Error: {e}")
        Speak("Unable to skip forward.")

# Function to skip backward 10 seconds
def YouTubeSkipBackward():
    try:
        press('left')  # Left arrow key skips backward 10 seconds
        Speak("Skipped backward 10 seconds.")
    except Exception as e:
        print(f"Error: {e}")
        Speak("Unable to skip backward.")

# Function to run speed test
def SpeedTest():
    try:
        Speak("Running a speed test, please wait...")
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        Speak(f"Your download speed is {download_speed:.2f} Mbps")
        Speak(f"Your upload speed is {upload_speed:.2f} Mbps")
    except Exception as e:
        print(f"Error: {e}")
        Speak("Unable to complete the speed test.")

# Function to fetch information from Wikipedia or Google
def About(query):
    query = query.replace("about", "").strip()
    Speak(f"Searching for {query}...")
    try:
        # Search Wikipedia
        result = wikipedia.summary(query, sentences=2)
        Speak(f"According to Wikipedia: {result}")
        print(f"Wikipedia: {result}")
    except wikipedia.exceptions.DisambiguationError as e:
        Speak("There are multiple results for this query. Searching Google instead.")
        web.open(f"https://www.google.com/search?q={query}")
    except Exception as e:
        Speak("Couldn't find an answer on Wikipedia. Searching Google instead.")
        web.open(f"https://www.google.com/search?q={query}")

# Global variable to store images fetched from NASA API
mars_images = []
current_image_index = 0 

# Function to fetch and display Mars images
def MarsImages():
    global mars_images, current_image_index
    try:
        # NASA API Key
        nasa_api_key = ("add your nasa api") # Apni NASA API key yahan daali gayi hai
        rover_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={nasa_api_key}"  # 1000th day of Curiosity rover

        response = requests.get(rover_url)
        data = response.json()

        # Extracting the Mars image URLs
        mars_images = [photo['img_src'] for photo in data['photos']]

        if len(mars_images) > 0:
            current_image_index = 0
            Speak("Displaying the first Mars image.")
            web.open(mars_images[current_image_index])  # Open the first image in browser
        else:
            Speak("No Mars-related images found at this time.")
    except Exception as e:
        Speak("Unable to fetch Mars images.")
        print(f"Error: {e}")

# Function to show the next Mars image
def NextMarsImage():
    global current_image_index
    if len(mars_images) > 0:
        current_image_index = (current_image_index + 1) % len(mars_images)
        Speak(f"Displaying the next Mars image.")
        web.open(mars_images[current_image_index])  # Open the next image in browser
    else:
        Speak("No Mars images available to display.")

# Function to send a WhatsApp message
def SendWhatsAppMessage(contact_name, message):
    try:
        Speak(f"Sending WhatsApp message to {contact_name}.")
        startfile("WhatsApp.exe")  # Open WhatsApp desktop application
        time.sleep(5)  # Wait for WhatsApp to open

        # Search for contact
        click(x=200, y=100)  # Adjust coordinates as per your screen resolution
        write(contact_name)
        time.sleep(2)
        press("enter")

        # Type and send the message
        write(message)
        press("enter")
        Speak("Message successfully sent.")
    except Exception as e:
        Speak("Unable to send WhatsApp message.")
        print(f"Error: {e}")

# Function to make a WhatsApp call
def WhatsAppCall(contact_name):
    try:
        Speak(f"Calling {contact_name} on WhatsApp.")
        startfile("WhatsApp.exe")  # Open WhatsApp desktop application
        time.sleep(5)  # Wait for WhatsApp to open

        # Search for contact
        click(x=200, y=100)  # Adjust coordinates as per your screen resolution
        write(contact_name)
        time.sleep(2)
        press("enter")

        # Click on call button (adjust coordinates accordingly)
        click(x=1000, y=100)  # Replace with actual call button coordinates
        Speak("Call successfully initiated.")
    except Exception as e:
        Speak("Unable to make WhatsApp call.")
        print(f"Error: {e}")

# Function to open WhatsApp chats
def ShowWhatsAppChats():
    try:
        Speak("Opening WhatsApp chats.")
        startfile("WhatsApp.exe")  # Open WhatsApp desktop application
        time.sleep(5)  # Wait for WhatsApp to open
        Speak("WhatsApp chats are now open.")
    except Exception as e:
        Speak("Unable to open WhatsApp chats.")
        print(f"Error: {e}")

# Main Task Execution Function
def TaskExe():
    Speak("Hello! I am Nova. Please choose an input mode: voice or text.")
    print(": Choose your input mode - (1) Voice Command (2) Text Command")
    mode = input(": Enter 1 for Voice or 2 for Text: ")

    while True:
        if mode == "1":
            query = TakeCommand()
        elif mode == "2":
            query = PromptCommand()
        else:
            Speak("Invalid choice. Defaulting to text input.")
            mode = "2"
            query = PromptCommand()

        if not query:
            Speak("Sorry, I didn't catch that. Please try again.")
            continue

        # Command Handling
        if 'youtube search' in query:
            query = query.replace("youtube search", "").strip()
            YouTubePlay(query)

        elif 'google search' in query:
            query = query.replace("google search", "").strip()
            Speak(f"Searching Google for {query}.")
            web.open(f"https://www.google.com/search?q={query}")

        elif 'speed test' in query:
            SpeedTest()

        elif 'mars images' in query:
            MarsImages()

        elif 'next' in query:
            NextMarsImage()

        elif 'about' in query:
            About(query)

        elif 'send whatsapp message' in query:
            Speak("Who do you want to send a message to?")
            contact = TakeCommand() if mode == "1" else PromptCommand()
            Speak("What message should I send?")
            message = TakeCommand() if mode == "1" else PromptCommand()
            SendWhatsAppMessage(contact, message)

        elif 'whatsapp call' in query:
            Speak("Who do you want to call?")
            contact = TakeCommand() if mode == "1" else PromptCommand()
            WhatsAppCall(contact)

        elif 'show chats' in query:
            ShowWhatsAppChats()

        elif 'exit' in query or 'quit' in query or 'bye' in query:
            Speak("Goodbye! Have a nice day.")
            break

# Start the task execution
TaskExe()   
