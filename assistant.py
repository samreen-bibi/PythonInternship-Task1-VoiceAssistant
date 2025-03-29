import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import wikipedia
import subprocess
import sys
import time

# Initialize speech engine globally
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Adjust speed
engine.setProperty('volume', 1)  # Set volume to max

def speak(text):
    """Speak the given text."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command from user and return text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce noise
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)  # Increased timeout
            command = recognizer.recognize_google(audio)  # Convert speech to text
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Didn't catch that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return ""
        except sr.WaitTimeoutError:  # Fix timeout issue
            print("No speech detected. Listening again...")
            return ""

def handle_command(command):
    """Process the user's spoken command."""
    if "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        today_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today_date}")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "weather" in command:
        speak("Opening weather website.")
        webbrowser.open("https://www.weather.com")

    elif "play music" in command:
        music_dir = "C:\\Users\\Public\\Music"
        try:
            songs = os.listdir(music_dir)
            if songs:
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                speak(f"Playing {song}")
            else:
                speak("No music found.")
        except Exception:
            speak("Error playing music.")

    elif "joke" in command:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call fake spaghetti? An impasta!"
        ]
        speak(random.choice(jokes))

    elif "news" in command:
        speak("Opening latest news.")
        webbrowser.open("https://www.bbc.com/news")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching for {query} on Wikipedia")
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results, please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information.")

    elif "shutdown computer" in command:
        speak("Shutting down the computer.")
        os.system("shutdown /s /t 1")

    elif "restart computer" in command:
        speak("Restarting the computer.")
        os.system("shutdown /r /t 1")

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.run("notepad.exe")

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.run("calc.exe")

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day.")
        sys.exit()

    else:
        speak("Sorry, I didn't understand that.")

def main():
    """Continuously listen for voice commands."""
    speak("Voice Assistant Activated. How can I help you?")

    while True:
        command = listen()
        if command:
            handle_command(command)
        time.sleep(1)  # Prevents excessive CPU usage

if __name__ == "__main__":
    main()
