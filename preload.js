window.addEventListener('DOMContentLoaded', () => {

    const fetch = require('node-fetch');
    
    var data = document.getElementById('data');
    
    fetch('http://localhost:8888/')
    .then(res => res.json())
    .then(json => {
      Object.keys(json).forEach((key) => 
      {
        data.innerHTML += `<div><label><strong>${key}</strong></label> : ${json[key]}</div>`;
      })
    })
    .catch((error) => {
      data.innerHTML = "Unable to get data from server";
    })
})