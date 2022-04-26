const express = require('express');
const SpotifyWebAPI = require('spotify-web-api');

const app = express();

app.post('/login', (req, res) => {
    const code = req.body.code
    const SpotifyWebAPI = new SpotifyWebAPI({
        redirectUri: 'http://localhost:3000' ,
        clientId: ' c3a421d34ad145e4b76859e547a44bf7',
        clientSecret: ' 0214ef6ffacb4b73ad7c0cf7314204d3'
    })
})