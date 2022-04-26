import "bootstrap/dist/css/bootstrap.min.css"
import  Login from "./login";
import React from "react";
import Dashboard from "./Dashboard";


const code = new URLSearchParams(window.location.search).get('code')

function App() {
	return  <Dashboard code = {code} /> 
}

export default App
