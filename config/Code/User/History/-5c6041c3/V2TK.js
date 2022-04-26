import { Container } from "react-bootstrap";
import React from "react";

const AUTH_URL = "https://accounts.spotify.com/authorize?client_id=c3a421d34ad145e4b76859e547a44bf7&response_type=code&redirect_uri=https://localhost:3000&scope=streaming%20user-read-email%20user-read-private%20user-library-read%20user-library-modify%20user-read-playback-state%20user-modify-playback-state"

export default function Login()
{
	return(
		<Container 
		className = "d-flex justify-content-center align-items-center"
		style={{minHeight:"100vh"}}>
		<a className="btn btn-success btn-lg" href = {AUTH_URL}>Login
		Spotify</a> 
		</Container>
	)
}

