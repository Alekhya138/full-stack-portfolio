const button = document.querySelector("#probtn");
const head =document.querySelector("#mainhead")
button.addEventListener("click", function(){
    head.textContent="Welcome to My Projects"

});
const themeButton = document.querySelector("#themeb");
let isDark = true;
themeButton.addEventListener("click", function(){
    if(isDark){
        document.body.style.backgroundColor = "white";
        document.body.style.color = "black";
        isDark = false;
    } else {
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
        isDark = true;
    }

});
const exp1Button = document.querySelector("#exp1b");
exp1Button.addEventListener("click", function(){
    window.open("https://github.com/alekhya138" , "_blank");
});
const exp2Button = document.querySelector("#exp2b");
exp2Button.addEventListener("click", function(){

    window.open("https://github.com/alekhya138" , "_blank");
});
const exp3Button = document.querySelector("#exp3b");
exp3Button.addEventListener("click", function(){
    window.open("https://github.com/alekhya138" , "_blank");
});
const form = document.querySelector("#contactForm");
const nameInput = document.querySelector("#nameInput");
const emailInput = document.querySelector("#email");
const messageInput = document.querySelector("#message");
form.addEventListener("submit", function(event){
    event.preventDefault();
    if(nameInput.value==="" || emailInput.value==="" || messageInput.value===""){
        alert("Please fill in all fields before submitting.");
    }
   else {
        alert("Thank you for your message, " + nameInput.value + "! I will get back to you soon.");
        form.submit(); // <-- Add this line to manually send the data to Flask!
    }
    
});
