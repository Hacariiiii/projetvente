
let colorss=document.querySelector('.dowara');
let btn=document.querySelector('#mo3a9');
let list=document.querySelector('.bibibi');
let hihi=document.querySelector('.haha')


btn.addEventListener('click', ()=>{
    let nt = document.createElement('div') ;
    nt.classList.add('note');
    nt.innerHTML=  ` 
    
        <textarea name="" class="s" rows="20" placeholder="Write here...."></textarea>
        <span class="haha">x</span>
    
`;

console.log(colorss.value);
nt.style.borderColor=colorss.value;
list.appendChild(nt);
fadeInElement(nt)

  



});


document.addEventListener("click", (event) => {
    console.log(event.target);

    if (event.target.classList.contains('haha')) {
        const element = event.target.parentNode;

        // Start the fade-out animation
        let opacity = 1; // Initial opacity
        const fadeDuration = 2000; // Duration of the fade-out in milliseconds (2 seconds)
        const interval = 50; // Interval time in milliseconds for updating opacity

        const fadeEffect = setInterval(() => {
            if (opacity > 0) {
                opacity -= interval / fadeDuration; // Decrease opacity over time
                element.style.opacity = opacity;
            } else {
                clearInterval(fadeEffect); // Stop the interval when fully faded out
                element.remove(); // Remove the element from the DOM
            }
        }, interval);
    }
});










function fadeInElement(element, duration = 2000, interval = 80) {
    let opacity = 0; // Start opacity at 0 for fade-in effect

    // Set the initial opacity to 0
    element.style.opacity = opacity;

    const fadein = setInterval(() => {
        if (opacity < 1) {
            opacity += interval / duration; // Increase opacity gradually
            element.style.opacity = opacity;
        } else {
            clearInterval(fadein); // Stop the interval when fully faded in
        }
    }, interval);
}




dd=document.querySelector('.header')
cont=document.querySelector('.cont')

const selectobserver= new IntersectionObserver((entries)=>{

    entries.forEach((entry)=>{
        if(!entry.isIntersecting)
        {
            dd.classList.add("dd")
            

        }
        else
            {
               dd.classList.remove("dd")
                
    
            }

    });


});

selectobserver.observe(cont)


moraba3=document.querySelector('.moraba3')


const conserv = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
        if(entry.isIntersecting)
        {
            dd.classList.add("rr")
        }
        else
            {
                dd.classList.remove("rr")
            }

    });




});
conserv.observe(moraba3)


const about = document.querySelector('.about');
const simo = document.querySelector('.simo');

about.addEventListener('click', (event) => {
    event.preventDefault();

    // Calculate the scroll position with a 300px offset
    const simoTop = simo.getBoundingClientRect().top + window.scrollY - 88;

    // Use window.scrollTo instead of scrollIntoView
    window.scrollTo({
        top: simoTop,
        behavior: 'smooth'
    });
});


footer=document.querySelector('.footerr')
fooder=document.querySelector('.footer')

footer.addEventListener('click', (event)=>{
    event.preventDefault()
    footer = fooder.getBoundingClientRect().top + window.scrollY-30;

    window.scrollTo({
        top: footer,
        behavior:'smooth'
    });



});


const prev = document.querySelector('.previous');
const next = document.querySelector('.next');
const zzz = document.querySelectorAll('.cont');

const number = cont.length;

let counter = 0;

// Liste des URLs pour les images


prev.addEventListener('click', () => {
    counter = counter - 1;
    if (counter < 0) {
        counter = number - 1; // Revenir au dernier élément si on dépasse le premier
    }
    showcount();
});

next.addEventListener('click', () => {
    counter = counter + 1;
    if (counter >= number) {
        counter = 0; // Revenir au premier élément si on dépasse le dernier
    }
    showcount();
});

function showcount() {

    let item=document.querySelector('.cont .active ')
    item.classList.remove('active')
   


    cont[counter].classList.add('active');



  
}



cvvv=document.querySelector('.home')

const YASSER = new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
    console.log(entry)

    });




});
YASSER.observe(cvvv)