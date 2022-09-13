import React from 'react'
import './Modal.css'

function Modal({openModal, onClose}) {

    if(!openModal) return null

    const OVERLAY_STYLES = {
        position: 'fixed',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.5)',
        zIndex: 100
    }

  return (
    <>
        <div style={OVERLAY_STYLES}/>
        <div className="modal">
            <button className="btn-modal" onClick={onClose}>X</button>
            <br />
            This the place where u explain what spotifyPR is,what tools did you use and how is it created.
        </div>
    </>
  )
}

export default Modal