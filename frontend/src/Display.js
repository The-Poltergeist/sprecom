import React, {useState,useEffect,useRef} from 'react'
import axiosInstance from './api';
import "./Display.css"
import SpotifyLogo from './Logo.png'
import Modal from './Modal';

function Display() {

  //states
  const ref = useRef(null);
  const [obj, setObj] = useState({link: "",track: 0});
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [valid, setValid] = useState(false);
  const [playlist, setPlaylist] = useState([]);
  const [error, setError] = useState('');
  const [modal, setModal] = useState(false);

  useEffect( () => {

    const makeRequest = async() => {
        try {
            setLoading(true);
            const res = await axiosInstance.post("form", {
                playlist_url: obj.link,
                number_of_recs: obj.track
            });
            console.log(res);
            setPlaylist(res.data.data);
            setLoading(false);
            //console.log(res);

        } catch (error) {
            setLoading(false);
            setError(error.response.data.remark);
        }
    }
    // console.log(obj);
    submitted && valid && makeRequest();

  },[obj, submitted, valid])


  //handler functions
  const inputLinkHandler = (e) => {
    setValid(false)
    setObj({...obj, link: e.target.value})
  } 
  const inputTrackHandler = (e) => {
    setValid(false)
    setObj({...obj, track: e.target.value})
  } 
  const submitHandler = (e) => {
    if(obj.link && obj.track && obj.track <= 40){
      setValid(true);
    }
    setSubmitted(true);
  }

  return (
    <>
    <div className='container'>
        <div className='main'>
          <div style={{display: 'flex', alignItems: 'center'}}>
          <img src={SpotifyLogo} alt="SpotifyLogo" />
          Spotify-PR
          </div>
          <div className='about'>
            <button className='btn-about'onClick={()=>{setModal(true); console.log('clicked')}}>About</button>
            
            <Modal openModal={modal} onClose={()=>{setModal(false)}}></Modal>
            
          </div>
        </div>
          <div ref={ref} className="form-container">
          <div className="form-dialog-box">
            {/* {submitted && valid && <div>success</div>} */}
            {/* {alert("success")} */}
            {loading && <div>Loading...</div>}
            {error !== '' && <div>{error}</div>}
              <input 
              className = "form-field"
              name="link"
              onChange={inputLinkHandler}
              placeholder="enter playlist url"
              value = {obj.link}/>
              {submitted && !obj.link ? <span>please enter a url</span> : null }
              <br/>
              
              <input 
              className = "form-field"
              name="track"
              onChange={inputTrackHandler}
              placeholder="number of tracks"
              value = {obj.track}/>
              {submitted && (!obj.track  || obj.track>40) ? <span>enter a value (max: 40)</span>: null} 
              <button onClick={submitHandler} className="btn-form">Recommend !</button>
          </div>
          {/* {console.log('hello')}   */}
          {submitted && valid && <div className="results-table">
            <div>
              <h1>Recommended for you</h1>
            </div>  
            <table>
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Link</th>
                </tr>
              </thead>
              <tbody>
              {
                playlist.map((val,index)=>{
                  return (
                    <tr key={index}>
                      <td>{val[0]}</td>
                      <td><a href= {`${val[1]}`} target="_blank" rel="noreferrer">{val[1]}</a></td>
                    </tr>
                  ) 
                })
              }
              </tbody> 
            </table>
          </div>
        }
      </div>
    </div>
    
    
    </>
  )
}

export default Display