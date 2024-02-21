const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');

0
let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width:  800,
        height:  600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true, // Add this line to enable access to remote modules
            webSecurity: false // Add this line to disable web security temporarily (for testing only)
        }
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);

ipcMain.on('open-camera', (event) => {
    // Here, you can add code to open the camera using Electron's getUserMedia API
    const constraints = {
        video: true,
        audio: false
    };

    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            console.log('Camera opened successfully');
            // You can handle the stream here, e.g., display it in a video element in the HTML
        })
        .catch((error) => {
            console.error('Error opening camera:', error);
            // You can send the error back to the renderer process if needed
            mainWindow.webContents.send('camera-error', error.toString());
        });


/* ipcMain.on('open-camera', (event) => {
    // Spawn a child process to run the camera.py script
    ipcMain.on('open-camera', (event) => {
    // Here, you can add code to open the camera using Electron's getUserMedia API
    const constraints = {
        video: true,
        audio: false
    };

    navigator.mediaDevices.getUserMedia(constraints)
        .then((stream) => {
            console.log('Camera opened successfully');
            // You can handle the stream here, e.g., display it in a video element in the HTML
        })
        .catch((error) => {
            console.error('Error opening camera:', error);
            // You can send the error back to the renderer process if needed
            mainWindow.webContents.send('camera-error', error.toString());
        });const cameraProcess = spawn('python', ['augmented_pc/phase_one/python/camera.py']);

    cameraProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
        // You can send the data back to the renderer process if needed
        mainWindow.webContents.send('camera-output', data.toString());
    });
  

    cameraProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        mainWindow.webContents.send('camera-error', data.toString());

    });

    cameraProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });*/
});

