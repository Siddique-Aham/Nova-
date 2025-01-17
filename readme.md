# Nova AI Assistant

Nova is a personal AI assistant capable of performing a variety of tasks based on voice or text input. It integrates various features like Google search, YouTube search, alarm setting, WhatsApp messaging and calling, space news, Mars image fetching, ISS tracking, and more.

## Features
- **Basic Tasks**: 
  - Google Search
  - YouTube Search
  - Set Alarm
  - Speed Test
  - WhatsApp Messaging, Calling, and Chat Viewing

- **Advanced Tasks**: 
  - NASA News Fetching
  - Mars Image Display
  - ISS Tracking
  - Near-Earth Asteroid Data

## Technologies Used
- **Python**: The primary programming language.
- **Libraries**:
  - `pyttsx3`: For text-to-speech conversion.
  - `speech_recognition`: For voice command recognition.
  - Custom Modules: 
    - `Features`: Contains functionalities like Google search, YouTube search, etc.
    - `Automations`: Handles WhatsApp tasks.
    - `Nasa`: Fetches space-related news and information.

## Installation
1. Install required libraries:
   ```bash
   pip install pyttsx3 speechrecognition
