   # A Basic Voice Enabled chat-bot in Python<br>

**This Project is still being developed, only recognizes voice for now**

Building a Voice Enabled chat-bot in Python which does basic tasts like telling you the weather in your area, lauches google/youtube, tells jokes, etc.

This project is a tutorial on how to build a chat-bot in python that recognizes speech in English only.

This project is done solely in Python and the commands are for Linux and Windows(Anaconda Prompt).

Before diving into the implementation we need to install the required libraries/modules for this project.

To install the required libraries run the following commands in your terminal : 

___

   ## How to Run :
   
Run the following commands in three different terminals :
   
*Terminal 1 :*
```rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml```

*Terminal 2 :*
```rasa run actions```

*Terminal 3 :*
```python Voice_bot.py```

<br>

****

# Input Audio device :

Make sure your audio device is setup right. 

Try to record an audio note using your system's audio recorder to test if your input device is connected and running. The Bot will not warn/show errors if it isnt able to detect any sound, it will only say : "Could not understand the audio" instead of no audio detected.

___

