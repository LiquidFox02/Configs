import "bootstrap/dist/css/bootstrap.min.css"
import  Login from "./login";
import React from "react";
//import Dashboard from "./Dashboard";


//const code = new URLSearchParams(window.location.search).get('code')

function App() {
	const [counter , setCounter] = useState(0)

	const handleClick = ()=>{
		setCounter(counter+1)	
		console.log("hey")
	}
	return(
	
		<div>
		<h2>{counter}</h2>
		<button onclick={handleClick} >Counter Increment</button>
		</div>
		
		
	)
}

export default App
