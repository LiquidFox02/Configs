const express = require('express');
const SpotifyWebApi = require('spotify-web-api');

const app = express();

app.post('/login', function(req, res) => {
    const code = req.body.code
    const spotifyApi = new SpotifyWebApi({
        redirectUri: 'https://localhost:3000' , 
        clientId: ' c3a421d34ad145e4b76859e547a44bf7' ,
        clientSecret: ' 0214ef6ffacb4b73ad7c0cf7314204d3'
    })
    spotifyApi.authorizationCodeGrant(code).then(data => {
        res.json({
            accessToken: data.body.access_token,
            refreshToken: data.body.refresh_token,
            expiresIn: data.body.expires_in
        })
    }).catch(()=>{
        res.sendStatus(400)
    })
})