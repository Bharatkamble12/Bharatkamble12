
const menuToggle=document.getElementById("menu-toggle");
const navMenu=document.getElementById("navMenu");
menuToggle.addEventListener("click",()=>{
    navMenu.classList.toggle("hidden");
    navMenu.classList.toggle("translate-x-full");
    navMenu.classList.toggle("translate-x-0");
});
//Hide navMenu When a nav link is clicked(on mobile)
document.querySelectorAll(".nav-link").forEach(link=>{
    link.addEventListener("click",()=>{
        if(window.innerWidth<768){
            navMenu.classList.add("hidden");
            navMenu.classList.add("translate-x-full");
            navMenu.classList.remove("translate-x-0");
        }
    });
});