// app/index.js
const express = require('express');
const http = require('http');
const socketio = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketio(server);

// Serve the video streaming page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Socket.io connection handling
io.on('connection', (socket) => {
  console.log('A new user connected');
  socket.on('disconnect', () => {
    console.log('A user disconnected');
  });
});

const port = process.env.PORT || 3000;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
