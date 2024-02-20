import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

const { ipcRenderer } = require('electron');

ipcRenderer.on('camera-output', (event, data) => {
  console.log(data);
  // Handle the output data as needed, e.g., display it in the app
});

ipcRenderer.on('camera-error', (event, error) => {
  console.error(error);
  // Handle the error as needed, e.g., display an error message in the app
});


document.getElementById('camera').addEventListener('click', () => {
    // Send a message to the main process to open the camera
    ipcRenderer.send('open-camera');
});

