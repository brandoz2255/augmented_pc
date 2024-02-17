const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    offscreen: true, // Enable offscreen rendering
    contextIsolation: false, // Disable context isolation (not recommended for security)
    webPreferences: {
      nodeIntegration: true
    }
  });

  win.loadFile(path.join(__dirname, 'index.html'));
}

app.on('ready', createWindow);

