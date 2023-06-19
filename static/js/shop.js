let buttons = document.getElementsByClassName('Button')
for (let button in buttons ){
    buttons[button].addEventListener('click',(e)=>{
       if (user != 'AnonymousUser'){
         itemid = e.target.dataset.id 
         action = e.target.dataset.action
         console.log(itemid,action)
         csrftoken = getCookie('csrftoken')
         url = '/delete/'
         options = {
            method : 'POST',
            headers : {
                'Content-Type': 'application/json',
                'X-CSRFToken' : csrftoken,
            },
            body : JSON.stringify({'itemid': itemid , 'action' : action})
         }
         fetch(url,options).then(response => response.json()).then(data => {console.log(data)
         location.reload()})
       }
    

    })
}