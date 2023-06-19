let actions = document.getElementsByClassName('action-button')


for(let i = 0; i<actions.length; i++){
   actions[i].addEventListener('click', (e)=>{
   if(user == 'AnonymousUser' ){
       let productid = ''
       let action = ''
   }
   else{
       
       let productid = e.target.dataset.id
       let action = e.target.dataset.action
      
       console.log(action)
       console.log(productid)
       var csrfToken = getCookie('csrftoken');
   let url = '/changeproduct/'
   let options = {
       method: 'POST',
       headers: {
               'Content-Type': 'application/json',
               'X-CSRFToken' : csrfToken
           },
       body : JSON.stringify({ 'product' : productid, 'action' : action})
   }
   fetch(url,options).then(response => response.json()).then(data => {console.log(data)
   location.reload() 
   let paragraph = document.getElementById('paragraph')
   paragraph.innerText = `product has been added click the square or shopping bag below`})
   } 
   })

}