# ✅ PROJECT - DECODING THE LANGUAGE OF HANDS

### 🔹About the project :-
- "Tkinter" is a Python library specifically designed for creating user-friendly graphical user interfaces (GUIs).
-  "Python" It provides the core structure for processing user inputs and interacting with YOLOv3. 
- "GoogleTrans" is an open-source python library which provides an interface to translate various languages within the python program. (Bash Command : pip install googletrans)

We used various libraries like,
* PIL (or) Pillow - For image processing in python. (Filtering, image enhancement, and color operations etc.) (Bash Command : pip install pillow)
* OpenCV - For Image and Video Processing.
* NumPy - For handling and manipulating numerical data which extracted from hand gestures.

From Deep Learning based approaches, we used-
* Convolutional Neural Networks (CNN) – Used for image-based gesture recognition (e.g., hand shapes, facial expressions).
* YOLO (You Only Look Once) – Used for real-time hand detection in sign language. (Unlike other algorithms, YOLO processes an image in a single neural network pass, making it fast.)
* MediaPipe by Google – Real-time hand tracking and gesture recognition. (It is used to Capture video input using OpenCV and converts detected signs into text & speech output.)

### Difficulties faced ??
> While implementing the model using the YOLOv3 algorithm, we faced major challenges with localization, as it sometimes produced inaccurate bounding boxes for closely placed or irregularly shaped gestures.

> Translating sign language into spoken or written language was challenging due to complex linguistic rules, and achieving real-time recognition with low latency was essential for making the application practically usable — we used Googletrans for language translation.

### 🔹Working Demonstration of the Project :- 
---
The comprehensive working of the project, including the conversion of hand signs from datasets into text (via static images) and dynamic recognition through webcam access, can be demonstrated in the implementation video linked below.

https://github.com/MadhuNadhGurram/Decoding_the_Language_of_Hands-Machine_Learning_in_Sign_Language/assets/84019306/fedb2396-6ce0-4345-8400-d02e7d3861fd

### 🔹Abstract :-
---
A comprehensive solution aimed at revolutionizing communication for deaf and  mute individuals, particularly in critical situations. We address the communication gap through a groundbreaking vision-based technique for hand gesture recognition. The core of our system lies in real-time hand gesture tracking libraries. These libraries are empowered by the YOLO (You Only Look Once) object detection algorithm, renowned for its accuracy. This translates to a system that can precisely identify and classify the various signs used in sign language. Unlike traditional methods that may require specialized equipment or specific environments, our vision-based approach boasts superior adaptability. Deaf and mute users can effectively convey messages in diverse settings, ensuring clear and unhindered communication regardless of the situation.
 
Our project transcends mere gesture recognition. We seamlessly integrate cutting edge voice conversion technologies, including a Text-to-Speech (TTS) system. This crucial step bridges the gap between sign language and spoken communication. The identified signs are translated into human-hearable voice (typically English), enabling effective interaction with individuals unfamiliar with sign language. This fosters a more inclusive environment where everyone can participate in the conversation. In essence, this project that leverages the power of vision technology to break down communication barriers for deaf and mute individuals. By offering a system that combines accurate gesture recognition with real-time voice conversion, we pave the way for a more connected society where everyone has a voice.

### 🔹Algorithm & Module used for the Project :-
---

1. Tkinter (Module)
   
Tkinter is a graphical user interface (GUI) module for Python, you can make desktop apps with Python. You can make windows, buttons, show text and images amongst other things. The module Tkinter is an interface to the Tk GUI toolkit. Tkinter is the most commonly used library for developing GUI in Python. It is a standard Python interface to the Tk GUI toolkit shipped with Python.
To Install the Tkinter, Open up the command prompt and use the below command:

       pip install tk

2. YOLO - You Only Look Once (Algorithm)

You Only Look Once (YOLO) is a powerful neural network architecture that excels in real-time object detection. It is the Algorithm we used in the Project to detect the Signs with Accuracy.

It Empowers-
~ Object Detection Expertise
~ Real-Time Performance 
~ Single-Stage Advantage

### 🔹Libraries Used for the Project :-
---
1. PIL :
It Stands for Python Imaging Library (PIL), which is now known as Pillow. It is a powerful library for working with images in Python and provides extensive image processing capabilities, file format support, and efficient internal representation for Python. The core image library is designed for fast access to data stored in basic pixel formats.
It has the Features like,
* Image Processing: Pillow allows you to perform various image manipulation tasks, such as resizing, cropping, filtering, and more.
* File Format Support: It can open, manipulate, and save many different image file formats.
* Documentation: Pillow comes with comprehensive documentation to guide you through its usage.
You can install Pillow using pip:

      pip install pillow

2. OpenCV :
is a Python library that is used to study images and video streams. It basically extracts the pixels from the images and videos (stream of image) so as to study the objects and thus obtain what they contain. It contains low-level image processing and high-level algorithms for object detection, feature matching etc.
To install OpenCV using pip, you can run the following command in your terminal or command prompt:

       pip install opencv-python

3. NumPy :
is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
If you use pip, you can install NumPy with:
       
       pip install numpy

