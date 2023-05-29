Naziya = "Naziya"

document.addEventListener("keydown", e =>{
    if (
        e.key.toLowerCase() === "i"
        && e.ctrlKey 
    ){
        var r = document.querySelector(':root');
        var rs = getComputedStyle(r);
        const random_color = () => {
            let n = (Math.random() * 0xfffff * 1000000).toString(16);
            return '#' + n.slice(0,6);
        }
        var color = random_color()
        r.style.setProperty('--accent-color', color);
        document.getElementById("colorChoice").value = color;
        document.getElementById("colorChoicemid").value = color;
        localStorage.setItem("Naziya" , color)
}
});

var r = document.querySelector(':root');
var r1 = document.querySelector(':root');


function changeColor(){
    var rs = getComputedStyle(r);
    document.getElementById("colorChoice").addEventListener('change', (e) => {
    
    let color = e.target.value
    localStorage.setItem("Naziya" , color)
    r.style.setProperty('--accent-color', localStorage.getItem("Naziya"));
    
    document.getElementById("colorChoicemid").value = localStorage.getItem("Naziya");
});
};

function changeColormid(){
    var rs = getComputedStyle(r1);
    document.getElementById("colorChoicemid").addEventListener('change', (e) => {
    
    let color = e.target.value
    localStorage.setItem("Naziya" , color)
    r1.style.setProperty('--accent-color', localStorage.getItem("Naziya"));
    document.getElementById("colorChoice").value = localStorage.getItem("Naziya");

});
};

r.style.setProperty('--accent-color', localStorage.getItem("Naziya"));
r1.style.setProperty('--accent-color', localStorage.getItem("Naziya"));

console.log(localStorage.getItem("--accent-color"))

if (localStorage.getItem("Naziya") === null){
    document.getElementById("colorChoice").value = "#ff0000";
    document.getElementById("colorChoicemid").value = "#ff0000";
}
else{
    console.log(localStorage.getItem("Naziya"))
    document.getElementById("colorChoice").value = localStorage.getItem("Naziya");
    document.getElementById("colorChoicemid").value = localStorage.getItem("Naziya");
}    

var naziya5= document.getElementById("naziya5");
var naziya51= document.getElementById("naziya51");

naziya5.onclick= function() {
    document.body.classList.toggle("white-theme");
    if(document.body.classList.contains("white-theme")) {
        localStorage.setItem("theme" , "white")
        naziya5.classList.add('themeclickanimation');
        naziya5.classList.remove('themeclickanimation1');
        naziya51.classList.add('themeclickanimation');
        naziya51.classList.remove('themeclickanimation1');
        naziya5.src = "/static/Assets/moon(1).png"; 
        naziya51.src = "/static/Assets/moon(1).png";
        home1.src = "/static/Assets/home.png"
        name1.src = "/static/Assets/name-icon.png"
        phone1.src= "/static/Assets/phone.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(Black).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypo.png"

    }
    else{
        localStorage.setItem("theme" , "black")
        naziya5.classList.add('themeclickanimation1');
        naziya5.classList.remove('themeclickanimation');
        naziya51.classList.add('themeclickanimation1');
        naziya51.classList.remove('themeclickanimation');
        naziya5.src = "/static/Assets/sun.png";
        naziya51.src = "/static/Assets/sun.png";
        home1.src = "/static/Assets/home1.png"
        name1.src = "/static/Assets/name-icon1.png"
        phone1.src= "/static/Assets/phone1.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(White).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypoW.png"

    }
}

naziya51.onclick= function() {
    document.body.classList.toggle("white-theme");
    if(document.body.classList.contains("white-theme")) {
        localStorage.setItem("theme" , "white")
        naziya51.classList.add('themeclickanimation');
        naziya51.classList.remove('themeclickanimation1');
        naziya5.classList.add('themeclickanimation');
        naziya5.classList.remove('themeclickanimation1');
        naziya51.src = "/static/Assets/moon(1).png"; 
        naziya5.src = "/static/Assets/moon(1).png"; 
        home1.src = "/static/Assets/home.png"
        name1.src = "/static/Assets/name-icon.png"
        phone1.src= "/static/Assets/phone.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(Black).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypo.png"
    }

    else{
        localStorage.setItem("theme" , "black")
        naziya51.classList.add('themeclickanimation1');
        naziya51.classList.remove('themeclickanimation');
        naziya5.classList.add('themeclickanimation1');
        naziya5.classList.remove('themeclickanimation');
        naziya51.src = "/static/Assets/sun.png";
        naziya5.src = "/static/Assets/sun.png"; 
        home1.src = "/static/Assets/home1.png"
        name1.src = "/static/Assets/name-icon1.png"
        phone1.src= "/static/Assets/phone1.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(White).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypoW.png"
    }
}

function myFunction(x) {
x.classList.toggle("change");
}

const Nazpar = document.querySelector(':root');
document.querySelector('.slider').addEventListener('input', (e) => {
  Nazpar.style.setProperty('--position', `${e.target.value}%`);
})

const container78 = document.querySelector(':root');
document.querySelector('.slider78').addEventListener('input', (e) => {
  container78.style.setProperty('--position78', `${e.target.value}%`);
})

const container786 = document.querySelector(':root');
document.querySelector('.slider786').addEventListener('input', (e) => {
  container786.style.setProperty('--position786', `${e.target.value}%`);
})

const containernaz = document.querySelector(':root');
document.querySelector('.slidernaz').addEventListener('input', (e) => {
  containernaz.style.setProperty('--positionnaz', `${e.target.value}%`);
})


const containernaz1 = document.querySelector(':root');
document.querySelector('.slidernaz1').addEventListener('input', (e) => {
  containernaz1.style.setProperty('--positionnaz1', `${e.target.value}%`);
})

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}

parnaz = document.getElementById("customID");

var myScrollFunc = function() {
    var y = window.scrollY;
    
    const contactformcolorchange2 = document.getElementById("contactform")
    const homecolorchange2 = document.getElementById("homechange")
    const workcolorchange2 = document.getElementById("workchange")

    if (y >= 300) {
        parnaz.className = "par show";
        contactformcolorchange2.style.color = 'var(--secondary-color)';
        homecolorchange2.style.color = 'var(--secondary-color)';
        workcolorchange2.style.color = 'var(--accent-color)';
    } else {
        parnaz.className = "par hide"
        contactformcolorchange2.style.color = 'var(--secondary-color)';
        homecolorchange2.style.color = 'var(--accent-color)';
        workcolorchange2.style.color = 'var(--secondary-color)';
    }
    };

window.addEventListener("scroll", myScrollFunc);

parnaz1 = document.getElementById("customID1");

var myScrollFunc = function() {
var y = window.scrollY;
if (y >= 900) {
    parnaz1.className = "par1 show"
} else {
    parnaz1.className = "par1 hide"
}
};

window.addEventListener("scroll", myScrollFunc);

parnaz2 = document.getElementById("customID2");
var myScrollFunc = function() {
var y = window.scrollY;
if (y >= 250) {
    parnaz2.className = "par2 show"
} else {
    parnaz2.className = "par2 hide"
}
};

window.addEventListener("scroll", myScrollFunc);

function scrolling(){
  window.scrollTo(0,330);
};

function scrollingtop(){
  window.scrollTo(0,0);
};

function scrollingdown(){
  window.scrollTo(0,999999);
};

const scrollL = document.getElementById('scrollleft');
scrollL.onclick = () =>{
    document.getElementById('scrollcontainer').scrollLeft -= 200;
};

const scrollR= document.getElementById('scrollright');
scrollR.onclick = () =>{
    document.getElementById('scrollcontainer').scrollLeft += 200;
};

document.addEventListener("keydown", e =>{
    if (
        e.key.toLowerCase() === "b"
        && e.ctrlKey
    ){
        document.body.classList.toggle("white-theme");
        if(document.body.classList.contains("white-theme")) {
            localStorage.setItem("theme" , "white")
            naziya5.classList.add('themeclickanimation');
            naziya5.classList.remove('themeclickanimation1');
            naziya51.classList.add('themeclickanimation');
            naziya51.classList.remove('themeclickanimation1');
            naziya5.src = "/static/Assets/moon(1).png";
            naziya51.src = "/static/Assets/moon(1).png"; 
            home1.src = "/static/Assets/home.png"
            name1.src = "/static/Assets/name-icon.png"
            phone1.src= "/static/Assets/phone.png"
            naztypo.src= "/static/Assets/NazTypoGraphy(Black).png"
            previewnaztypo.src = "/static/Assets/PreviewNazTypo.png"
        }
        else{
            localStorage.setItem("theme" , "black")
            naziya5.classList.add('themeclickanimation1');
            naziya5.classList.remove('themeclickanimation');
            naziya51.classList.add('themeclickanimation1');
            naziya51.classList.remove('themeclickanimation');
            naziya5.src = "/static/Assets/sun.png";
            naziya51.src = "/static/Assets/sun.png"; 
            home1.src = "/static/Assets/home1.png"
            name1.src = "/static/Assets/name-icon1.png"
            phone1.src= "/static/Assets/phone1.png"
            naztypo.src= "/static/Assets/NazTypoGraphy(White).png"
            previewnaztypo.src = "/static/Assets/PreviewNazTypoW.png"
        }
    }
});

z = localStorage.getItem("theme")
if (z == "white"){
    document.body.classList.toggle("white-theme");
    if(document.body.classList.contains("white-theme")) {
        localStorage.setItem("theme" , "white")
        naziya5.classList.add('themeclickanimation');
        naziya5.classList.remove('themeclickanimation1');
        naziya51.classList.add('themeclickanimation');
        naziya51.classList.remove('themeclickanimation1');
        naziya5.src = "/static/Assets/moon(1).png";
        naziya51.src = "/static/Assets/moon(1).png"; 
        home1.src = "/static/Assets/home.png"
        name1.src = "/static/Assets/name-icon.png"
        phone1.src= "/static/Assets/phone.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(Black).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypo.png"
    }
    else{
        localStorage.setItem("theme" , "black")
        naziya5.classList.add('themeclickanimation1');
        naziya5.classList.remove('themeclickanimation');
        naziya51.classList.add('themeclickanimation1');
        naziya51.classList.remove('themeclickanimation');
        naziya5.src = "/static/Assets/sun.png";
        naziya51.src = "/static/Assets/sun.png"; 
        home1.src = "/static/Assets/home1.png"
        name1.src = "/static/Assets/name-icon1.png"
        phone1.src= "/static/Assets/phone1.png"
        naztypo.src= "/static/Assets/NazTypoGraphy(White).png"
        previewnaztypo.src = "/static/Assets/PreviewNazTypoW.png"
    }
}


const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        if (entry.isIntersecting) {
            entry.target.classList.add('showanimation');
        }
        else{
            entry.target.classList.remove('showanimation');
        }
    });
});

const observer1 = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        if (entry.isIntersecting) {
            entry.target.classList.add('showanimation1');
        }
        else{
            entry.target.classList.remove('showanimation1');
        }
    });
});

const observer2 = new IntersectionObserver((entries) => {
    entries.forEach((entry) =>{
        if (entry.isIntersecting) {
            entry.target.classList.add('showanimation2');
        }
        else{
            entry.target.classList.remove('showanimation2');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hiddenanimation');
const hiddenElements1 = document.querySelectorAll('.hiddenanimation1');
const hiddenElements2 = document.querySelectorAll('.hiddenanimation2');
hiddenElements.forEach((el) => observer.observe(el));
hiddenElements1.forEach((el) => observer1.observe(el));
hiddenElements2.forEach((el) => observer2.observe(el));



// SHOW MOUSE SCROLL DIRECTION EITHER UP OR DOWN

var scrollableElement = document.body;
scrollableElement.addEventListener('wheel', checkScrollDirection);

function checkScrollDirection(event){
    if (checkScrollDirectionIsUp(event)) {
    }
    else{
    }
}

function checkScrollDirectionIsUp(event){
    if (event.wheelDelta) {
        return event.wheelDelta > 0;
    }
    return event.deltaY < 0;
}