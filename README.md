   # A Basic Voice Enabled chat-bot in Python<br>

Building a Voice Enabled chat-bot in Python which does basic tasts like telling you the weather in your area, lauches google/youtube, tells jokes, etc.

This project is a tutorial on how to build a chat-bot in python that recognizes speech in English only.

This project is done solely in Python and the commands are for Linux and Windows(Anaconda Prompt).

Before diving into the implementation we need to install the required libraries/modules for this project.

To install the required libraries run the following commands in your terminal : 

___

   ## How to Run :
   
 **Install dependencies by running**  
 
 We need to install the following libraries : **pyttsx3 | wikipedia | SpeechRecognition | pygame | pyown | pyaudio**
 
 Since we are using microphone interface(input from the microphone), we will need to install pyaudio.
 
 We dont need to install them separately, instead install all of them collectively by running the following command :
 
 For Linux Terminal : 
 
 ```pip install -r requirement.txt``` 
 
 OR
 
 ```pip3 install -r requirement.txt``` 
 
 For Windows [Anaconda Prompt] : 
 
 ```python -m pip install -r requirements.txt``` 
 
 **Running the main code**
 
 ```python main.py```
 

<br>

****

Make sure your audio device is setup right. 

Try to record an audio note using your system's audio recorder to test if your input device is connected and running. The Bot will not warn/show errors if it isnt able to detect any sound, it will only say : 



