Naziya = 'Naziya'
var naziya517= document.getElementById("naziya517");
    
naziya517.onclick= function() {
    document.body.classList.toggle("white-theme");
    if(document.body.classList.contains("white-theme")) {
        localStorage.setItem("theme" , "white")
        naziya517.classList.add('themeclickanimation');
        naziya517.classList.remove('themeclickanimation1');
        naziya517.src = "/static/Assets/moon(1).png";
        one1.src = "/static/Assets/name-icon.png";
        one2.src = "/static/Assets/mail.png";
        one4.src = "/static/Assets/phone.png";
        home1.src = "/static/Assets/home.png"
        name1.src = "/static/Assets/name-icon.png"
        phone1.src= "/static/Assets/phone.png"
        
    }
    else{
        localStorage.setItem("theme" , "black")
        naziya517.classList.add('themeclickanimation1');
        naziya517.classList.remove('themeclickanimation');
        naziya517.src = "/static/Assets/sun.png";
        one1.src = "/static/Assets/name-icon1.png";
        one2.src = "/static/Assets/mail1.png";
        one4.src = "/static/Assets/phone1.png";
        home1.src = "/static/Assets/home1.png"
        name1.src = "/static/Assets/name-icon1.png"
        phone1.src= "/static/Assets/phone1.png"
        
    }
}

document.addEventListener("keydown", e =>{
    if (
        e.key.toLowerCase() === "b"
        && e.ctrlKey
    ){
        document.body.classList.toggle("white-theme");
        if(document.body.classList.contains("white-theme")) {
            localStorage.setItem("theme" , "white")
            naziya517.classList.add('themeclickanimation');
            naziya517.classList.remove('themeclickanimation1');
            naziya517.src = "/static/Assets/moon(1).png";
            one1.src = "/static/Assets/name-icon.png";
            one2.src = "/static/Assets/mail.png";
            one4.src = "/static/Assets/phone.png";
            home1.src = "/static/Assets/home.png"
            name1.src = "/static/Assets/name-icon.png"
            phone1.src= "/static/Assets/phone.png"
        }

        else{
            localStorage.setItem("theme" , "black")
            naziya517.classList.add('themeclickanimation1');
            naziya517.classList.remove('themeclickanimation');
            naziya517.src = "/static/Assets/sun.png";
            one1.src = "/static/Assets/name-icon1.png";
            one2.src = "/static/Assets/mail1.png";
            one4.src = "/static/Assets/phone1.png";
            home1.src = "/static/Assets/home1.png"
            name1.src = "/static/Assets/name-icon1.png"
            phone1.src= "/static/Assets/phone1.png"
        }
    }
});

z = localStorage.getItem("theme")
if (z == "white"){
    document.body.classList.toggle("white-theme");
    if(document.body.classList.contains("white-theme")) {
        localStorage.setItem("theme" , "white")
        naziya517.classList.add('themeclickanimation');
        naziya517.classList.remove('themeclickanimation1');
        naziya517.src = "/static/Assets/moon(1).png";
        one1.src = "/static/Assets/name-icon.png";
        one2.src = "/static/Assets/mail.png";
        one4.src = "/static/Assets/phone.png";
        home1.src = "/static/Assets/home.png"
        name1.src = "/static/Assets/name-icon.png"
        phone1.src= "/static/Assets/phone.png"
    }
    else{
        localStorage.setItem("theme" , "black")
        naziya517.classList.add('themeclickanimation1');
        naziya517.classList.remove('themeclickanimation');
        naziya517.src = "/static/Assets/sun.png";
        one1.src = "/static/Assets/name-icon1.png";
        one2.src = "/static/Assets/mail1.png";
        one4.src = "/static/Assets/phone1.png";
        home1.src = "/static/Assets/home1.png"
        name1.src = "/static/Assets/name-icon1.png"
        phone1.src= "/static/Assets/phone1.png"
    }
}

