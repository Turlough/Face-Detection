# Overview
A python project using OpenCV's Haar Cascade to detect faces in a remote video stream.

You will need to provide the url of the video stream.

# Instructions
See also: https://ai.turloughcowman.ie/computer-vision/face-detector/

1. Clone and cd into the repository folder: 
```
cd Face-Detection
```
2. Initialize and activate a new virtual environment:
```
virtualenv venv
source -p python3 venv/bin/activate
```
3. Install dependencies:
```
pip3 install -r requirements.txt
```
4. To run *face_detection.py* on a stream hosted at, say *http://127.0.0.1:8081*:
```
python face_detection.py http://127.0.0.1:8081
```

Pressing keyboard key 'q' exits and closes the window.