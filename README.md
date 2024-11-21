# static_hand_gesture_recognition

## Dataset Preparation
To prepare the dataset, use the `extract_frames.py` script to extract frames from your image or video files (e.g., MP4). This process generates a series of images that will be used for training the gesture recognition model.

## Data Annotation
We used **Roboflow** for data labeling and augmentation. Roboflow makes it easy to annotate and enhance the dataset. Once the annotation process is complete, you can download the pre-labeled and augmented dataset from Roboflow.

### Dataset
- **Gesture Types**: open_palm, closed_fist, thumbs_up, v_sign

## API Key Setup
To use Roboflow's API, follow these steps:
 `!pip install roboflow`
```
from roboflow import Roboflow
rf = Roboflow(api_key=" ")
project = rf.workspace("gesturerecognition-9ztvg").project("static_hand_gesture_recognition")
version = project.version(1)
dataset = version.download("yolov5")
```
                

### YOLOv5 Integration
Clone the YOLOv5 repository. `git clone https://github.com/ultralytics/yolov5.git
`
Navigate to the YOLOv5 directory. `cd yolov5
`
Install the required dependencies for YOLOv5 using `pip install -r requirements.txt
` 

### Training YOLOv5s
Once YOLOv5 is set up and you have downloaded the dataset, you can begin training the model.


### Inference on Live Webcam
To perform inference on a live webcam, run the `webcam_inference.py` script. Ensure that your webcam is connected, and the script will use the webcam to detect gestures in real-time. 
`python webcam_inference.py`
