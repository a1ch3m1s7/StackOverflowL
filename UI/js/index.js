console.clear();
const navSlide =()=> {
    const burger = document.querySelector('.response_min');
    const nav =document.querySelector('.min_nav');
    const navLiens = document.querySelectorAll('.min_nav li');
   


    burger.addEventListener('click',()=>{
       //Toggle nav 
        nav.classList.toggle('min_nav-active');  
            
            //Animate links 
        navLiens.forEach((link,index) => {
          if(link.style.animation) {
                link.style.animation = '';
          }else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.5}s`;
          }
        });
          //response animation
        burger.classList.toggle('toggle');

      });   
};


navSlide();
