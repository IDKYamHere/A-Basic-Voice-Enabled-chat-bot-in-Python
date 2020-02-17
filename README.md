   # Building a Voice Enabled chat-bot in Python<br>

Voice Biometrics Authentication using GMM and Face Recognition Using Facenet and Tensorflow
___

   ## How to Run :
   
 **Install dependencies by running**  
 
 For Linux Terminal : 
 
 ```pip install pyttsx3``` 
 
 ``` pip install -r requirements.txt``` 
 
 For Windows [Anaconda Prompt] : 
 
 ```python -m pip install -r requirements.txt``` 
 
 ### 1.Run in Jupyter notebook - main.ipynb
 ___
 
 ### 2.Run in terminal in following way :
 
   **To add new user :**
   ```
     python3 add_user.py
   ```
   **To Recognize user :**
   ```
     python3 recognize.py
   ```
   **To Recognize until KeyboardInterrupt (ctrl + c) by the user:**
   ```
     python3 recognize_until_keyboard_Interrupt.py
   ```
   **To delete an existing user :**
   ```
     python3 delete_user.py
   ```
___
## Voice Authentication

   *For Voice recognition, **GMM (Gaussian Mixture Model)** is used to train on extracted MFCC features from audio wav           file.*<br><br>
     
## Face Recognition

  *Face Recognition system using **Siamese Neural network**. The model is based on the **FaceNet model** implemented using Tensorflow and OpenCV implementaion has been done for realtime face detection and recognition.<br>
The model uses face encodings for identifying users.<br><br>*
The program uses a python dictionary for mapping for users to their corresponding face encodings. <br>
___
<br>


**Controlling the face recognition accuracy:**
 The threshold value controls the confidence with which the face is recognized, you can control it by changing the value which is here 0.5. <br><br>



****

This project is a tutorial on how to build a chat-bot in python that recognizes speech in English.

This project is done solely in Python and the commands are for Linux and Windows(Anaconda Prompt).

Before diving into the implementation we need to install the requires libraries for this project.

To install the required libraries run the following commands in your terminal : 

''''''

'''pip install wikipedia'''  

'''pip install SpeechRecognition'''

'''pip install pygame'''

'''pip install pyown'''
