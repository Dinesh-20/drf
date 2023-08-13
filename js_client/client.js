const contentContainer = document.getElementById('content-container')
const loginForm = document.getElementById('login-form')
const baseEndpoint = 'http://localhost:8000/api'
if (loginForm) {
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {
    event.preventDefault()
    const loginEndpoint = `${baseEndpoint}/token/`
    let loginFormData = new FormData(loginForm)
    let loginOjectData = Object.fromEntries(loginFormData)
    console.log(loginOjectData)
    bodyStr = JSON.stringify(loginOjectData)
    console.log(bodyStr)
    const options = {
        method : 'POST',
        headers : {
            'Content-Type':'application/json'
        },
        body: bodyStr,
    }
    fetch(loginEndpoint, options)
    .then(response=>{
        console.log(response.json)
        return response.json
    })
    .then(authData =>{
        console.log(authData)
        handleAuthData(authData, getProductList)
    })
    .catch(err=>{
        console.log('err',err)
    })
}

function handleAuthData(authData, callback) {
    localStorage.setItem('access', authDataaccess)
    localStorage.setItem('refresh', authData.refresh)
    if (callback){
        callback()
    }
}

function writeToContainer(data){
    if (contentContainer){
        contentContainer.innerHTML = '<pre>' + JSON.stringify(data) + '</pre>'
    }
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = {
        method:'GET',
        headers:{
            'Content-Type':'application/json',
            'Authorization':`Bearer ${localStorage.getItem('access')}`
        }
    }
    fetch(endpoint, options)
    .then(response=>response.json)
    .then(data=>{
        writeToContainer(data)
    })
}