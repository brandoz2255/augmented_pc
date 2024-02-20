from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/open_camera', methods=['POST'])
def open_camera():
    try:
        # Execute the camera.py script
        subprocess.run(['python', 'augmented_pc/phase_one/python'], check=True)
        return 'Camera opened successfully',  200
    except Exception as e:
        return str(e),  500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)