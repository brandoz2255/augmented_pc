const { app, BrowserWindow, ipcMain } = require('electron');
const { spawn } = require('child_process');


let mainWindow;

function createWindow() {
    mainWindow = new BrowserWindow({
        width:  800,
        height:  600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(createWindow);

ipcMain.on('open-camera', (event) => {
    // Spawn a child process to run the camera.py script
    const cameraProcess = spawn('python', ['augmented_pc/phase_one/python/camera.py']);

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
    });
});
