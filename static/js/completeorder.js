let button = document.getElementById('Complete')

button.addEventListener('click',(e)=>{
    orderid = e.target.dataset.id
    action = e.target.dataset.action
    var csrfToken = getCookie('csrftoken')
    url = '/Completeorder/'

    options = {
        method : 'POST',
        headers : {
             'Content-Type' : 'application/json',
             'X-CSRFToken' : csrfToken
        },
        body : JSON.stringify({'order' : orderid, 'action': action})
    }
    fetch(url,options).then(response => response.json()).then(data => {
        console.log(data)
        location.reload()
    })
})