import React from 'react'
import "./Display.css"

function Display() {
  return (
    <div className='container'>
        <div className='main'>Spotify Recommender</div>
        <div className='about'>
            <div className='about-header'>
                About
            </div>
            <div className='about-body'>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            </div>
            <button className='btn'><span>Click to get recommendations</span></button>
        </div>
    </div>
    
  )
}

export default Display