import { Container } from "react-bootstrap";
import React from "react";
import {useState, useEffect} from 'react';

const AUTH_URL = "https://accounts.spotify.com/authorize?client_id=32f8d49555e64e679234706e9c1bb710&response_type=code&redirect_uri=http://localhost:3000&scope=streaming%20user-read-email%20user-read-private%20user-library-read%20user-library-modify%20user-read-playback-state%20user-modify-playback-state"

export default function Login()
{
	const [counter , setCounter] = useState(0);
	const handleClick = ()=>{
		setCounter(counter+1);	
			
	}
	return(
	
		<div>
		<h2>{counter}</h2>
		<button onclick={handleClick} >Counter Increment</button>
		</div>
		
		
	)
}

