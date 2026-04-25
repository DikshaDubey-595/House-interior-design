
window.addEventListener('scroll',function(){
let navbar= document.querySelector('.navbar');
if (window.scrollY > 20){
    navbar.classList.add('scrolled')
}else{
    navbar.classList.remove('scrolled')
}
})

let burger=document.querySelector('.burger')
let nav=document.querySelector('.nav')
let navbarItems=document.querySelector('.navbar-items')

burger.addEventListener('click',() =>{
    navbarItems.classList.toggle('h-class')
    nav.classList.toggle('v-class')
})

window.addEventListener('scroll',function(){
let navbar= document.querySelector('.navbar');
if (window.scrollY > 20){
    navbar.classList.add('scrolled')
}else{
    navbar.classList.remove('scrolled')
}
})

let burger=document.querySelector('.burger')
let nav=document.querySelector('.nav')
let navbarItems=document.querySelector('.navbar-items')

burger.addEventListener('click',() =>{
    navbarItems.classList.toggle('h-class')
    nav.classList.toggle('v-class')
})

