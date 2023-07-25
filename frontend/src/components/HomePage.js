import React from "react";
// Import our custom CSS
import '../scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

export default function HomePage(){
  return(
    <>
      <div className="container py-4 px-3 mx-auto">
        <h1>Hello world</h1>
        <button class="btn btn-primary">Primary button</button>
      </div>
    </>
  )
}