


import PySimpleGUI as sg
import cv2
import numpy as np

def cameraOpen():
    """
    This function will open up the camera, giving Python  
    control of my PC's camera
    """
    try:
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
        layout = [[sg.Image(key='-IMAGE-')],
                  [sg.Button('Exit')]]

        window = sg.Window('Camera', layout)
        return window
    except Exception as e:
        print("Error in windowCamera:", e)
        return None

def cameraVideo():
    """
    This function will capture the video streams to
    communicate with another function to analyze what it is seeing,
    basically the function to capture data from the camera  
    """
    try:
        camera = cameraOpen()
        if camera is None:
            return

        window = windowCamera()
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            # Convert the frame to bytes
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (640,  480))
            frame = cv2.flip(frame,  1)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame_bytes = cv2.imencode('.png', frame)[1].tobytes()
            window['-IMAGE-'].update(data=frame_bytes)

            event, values = window.read(timeout=20)
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break

        camera.release()
        window.close()
    except Exception as e:
        print("Error in cameraVideo:", e)

if __name__ == "__main__":
    cameraVideo()
