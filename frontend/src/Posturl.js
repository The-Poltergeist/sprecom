import React from 'react';
import axios from 'axios';

export default class Posturl extends React.Component{
    state = {
        sprec_url: ''
    }
    
    handlechange = event =>{
        this.setState({name:event.target.value});
    }

    handlesubmit = event =>{
        event.preventDefault();

        const user = {
            name: this.state.name
        };

        axios.post(`https://jsonplaceholder.typicode.com/users`, { user })
        .then(res => {
        console.log(res);
        console.log(res.data);
      })
    }

    render(){
        return 
    }
}
