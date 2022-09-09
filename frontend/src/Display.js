import React, {useState,useEffect,useRef} from 'react'
import axiosInstance from './api';
import "./Display.css"

function Display() {

  //states
  const ref = useRef(null);
  const [obj, setObj] = useState({link: "",track: 0});
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false);
  const [valid, setValid] = useState(false);
  const [playlist, setPlaylist] = useState([]);
  const [error, setError] = useState('');

  useEffect( () => {

    const makeRequest = async() => {
        try {
            setLoading(true);
            const res = await axiosInstance.post("form", {
                playlist_url: obj.link,
                number_of_recs: obj.track
            });
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
  const handleClick = ()=> {
    ref.current?.scrollIntoView({behavior: 'smooth', transition:'0.5s ease'});
  }
  const inputLinkHandler = (e) => {
    setValid(false)
    setObj({...obj, link: e.target.value})
  } 
  const inputTrackHandler = (e) => {
    setValid(false)
    setObj({...obj, track: e.target.value})
  } 
  const submitHandler = (e) => {
    // console.log(obj.link);
    // console.log(obj.track);
    // e.preventdefault();
    if(obj.link && obj.track && obj.track <= 40){
      setValid(true);
    }
    setSubmitted(true);
  }

  return (
    <>
    <div className='container'>
        <div className='main'>Spotify Recommender</div>
        <div className='about'>
            <div className='about-header'>
                About
            </div>
            <div className='about-body'>
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            </div>
            <button onClick={handleClick} className='btn'><span>Click to get recommendations</span></button>
        </div>
    </div>
    <div ref={ref} className="form-container">
        <div className="form-dialog-box">
          {submitted && valid && <div className="form-field">success</div>}
          {loading && <div>Loading...</div>}
          {error !== '' && <div>{error}</div>}
            <input 
            className = "form-field"
            name="link"
            onChange={inputLinkHandler}
            placeholder="enter playlist url"
            value = {obj.link}/>
            {submitted && !obj.link ? <span className="form-field">please enter a url</span> : null }
            <br/>
            
            <input 
            className = "form-field"
            name="track"
            onChange={inputTrackHandler}
            placeholder="number of tracks"
            value = {obj.track}/>
            {submitted && (!obj.track  || obj.track>40) ? <span className="form-field">enter a value (max: 40)</span>: null} 
            <button onClick={submitHandler}>Recommend !</button>
        </div>
    </div>
    </>
  )
}

export default Display