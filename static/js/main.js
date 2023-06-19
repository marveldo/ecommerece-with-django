
let bookonline = document.getElementById('bookonline')

let reviews = document.getElementById('reviews')

let close =document.getElementById('messages')

if(bookonline){
let hiddendiv = document.getElementById("hiddendiv")
let button1 = document.getElementById("showdiv")
let button2 = document.getElementById('closeform')
button1.onclick = () => {
    hiddendiv.style.display = 'grid'
}
button2.onclick = () => {
    hiddendiv.style.display = 'none'
}
}



if(reviews){
    let next = document.getElementById('next')
let prev = document.getElementById('prev')

let slideindex = 1

const plusslides = (n) => showslides(slideindex += n)





const showslides = (n) => {
   
    
    let slides = document.getElementsByClassName('slides')
   

    if(n>slides.length){
      slideindex = slides.length 
      next.style.display = 'none'
     
      
    }
    if(n<1){
        slideindex = 1
        prev.style.display = 'none'
      
    }
    for(let i =0 ; i<slides.length; i++){
        slides[i].style.display= 'none'
    }
   
    slides[slideindex - 1].style.display ='grid'
 console.log(slides[0])

}

    next.onclick =() => {
        plusslides(+1)
        prev.style.display = 'grid'
      
    }
    prev.onclick = () => {
        plusslides(-1)
      next.style.display = 'grid'
    }


    showslides(slideindex)

}
if(close){
    let closebutton = document.getElementById('close')
    let list = document.getElementById('list')
    closebutton.onclick = () => {
       list.style.display = 'none'
       console.log('deleted')
    }
}

