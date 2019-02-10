const express = require('express')
const app = express()
const port = 3000

app.get('/style.css', (req, res) => res.sendFile(__dirname + '/style.css'));

app.get('/client.js', (req, res) => res.sendFile(__dirname + '/client.js'));

app.get('/push', (req, res) => res.send("thanks, i hate it"));

app.post('/push', (req, res) => {
  res.send("gross, i love it");
  console.log('post received');
});

app.get('/', (req, res) => res.sendFile(__dirname + '/index.html'));

var server = app.listen(port, () => console.log(`Example app listening on port ${port}!`));

process.on('SIGTERM', () => {
  console.info('SIGTERM signal received.');
  server.close();
});

process.on('SIGINT', () => {
  console.info('SIGINT signal received.');
  server.close();
});
