

from yolov4.tf import YOLOv4

import os

import sys
sys.path.append("/home/dulc3/augmented_pc/phase_one/lib/pylib")

import cv2

def checkConnection():
    """
    This function will tell the test module 
    that this function has
    been called successfully
    """
    try:
        # Your implementation here
        print("Connection successful!")
    except Exception as e:
        print("Error in checkConnection:", e)

def cameraOpen():
    """
    This function will open up the camera, giving Python 
    control of my PC's camera
    """
    try:
        # Your implementation here
        camera = cv2.VideoCapture(0)
        return camera
    except Exception as e:
        print("Error in cameraOpen:", e)
        return None

def windowCamera():
    """
    This function will bring up the window to show the 
    camera being opened
    """
    try:
        # Your implementation here
        cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
    except Exception as e:
        print("Error in windowCamera:", e)

def cameraVideo():
    """
    This function will capture the video streams to
    communicate with another function to analyze what it is seeing,
    basically the function to capture data from the camera 
    """
    try:
        # Your implementation here
        camera = cameraOpen()
        if camera is None:
            return
        
        windowCamera()
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error in cameraVideo:", e)

def analyzeVideo():
    """
    This function will analyze the data and display it in the 
    bottom right of the window of the camera (in the same window), 
    telling the user what it sees
    """
    try:
        # Your implementation here
        camera = cameraOpen()
        if camera is None:
            return
        
        windowCamera()
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            # Perform image preprocessing and analysis here
            # For example, you can use OpenCV functions to detect objects or perform image processing
            # here is the converts the frame to grayscale 
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the analyzed result in the bottom right corner of the camera window
            cv2.putText(frame, "Analyzing...", (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
        camera.release()
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error in analyzeVideo:", e)


def checkOpenCVInstallation():
    try:
        # Check if OpenCV is installed
        version = cv2.__version__
        print(f"OpenCV version {version} is installed.")
    except ImportError:
        print("OpenCV is not installed.")



if __name__ == "__main__":
    checkOpenCVInstallation()
    cameraOpen()
    windowCamera()
    # Choose whether to run cameraVideo or analyzeVideo
    # cameraVideo()
    analyzeVideo()
