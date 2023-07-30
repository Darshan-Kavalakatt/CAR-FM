// app/public/client.js
const socket = io();

socket.on('connect', () => {
  console.log('Connected to server');
});

socket.on('disconnect', () => {
  console.log('Disconnected from server');
});

// Handle video stream
const video = document.getElementById('video');

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then((stream) => {
      video.srcObject = stream;
    })
    .catch((err) => {
      console.error('Error accessing the webcam:', err);
    });
}
