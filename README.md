# Overview
A python project using OpenCV's Haar Cascade to detect faces in a remote video stream.

You will need to provide the url of the video stream.

# Instructions
1. Clone and cd into the repository folder: 
```
cd Face-Detection
```
2. Edit the URL on line 8 of *face_detection.py* to match the URL of your video feed
3. Initialize and activate a new virtual environment:
```
virtualenv venv
source venv/bin/activate
```
4. Install dependencies:
```
pip3 install -r requirements.txt
```
5. To run *face_detection.py* on a stream hosted at, say *http://127.0.0.1:8081*:
```
python3 face_detection.py http://127.0.0.1:8081
```

Pressing keyboard key 'q' exits and closes the window.