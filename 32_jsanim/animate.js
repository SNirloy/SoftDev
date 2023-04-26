/*
James Yu, Sadi Nirloy 
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");
var screenButton = document.getElementById("dvdButton");

var ctx = c.getContext("2d");

var requestID;

var clear = (e) =>{
    e.preventDefault(); // To prevent some kind of unnecessary repetition
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;
var smaller = Math.min(c.width, c.height);

var drawDot = () => {
    // window.cancelAnimationFrame(requestID); // to prevent the acceleration of animation
    clear();
    ctx.beginPath(); // A path is needed in order to isolate steps in coloring
    ctx.fillStyle = "black"; //circle color
    ctx.strokeStyle = "black"; // outline color
    ctx.arc(c.width / 2, c.height / 2, radius, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();
    if (growing ){
        radius += 5;
    }else{
        radius -= 5;
    }

    if ( radius > smaller / 2 && growing){
        growing = false;
    }

    if (radius <= 0 && !growing){
        growing = true;
    }
    requestID = window.requestAnimationFrame(drawDot);
    dotButton.removeEventListener("click", drawDot); // I used this method to take away the power of the button to add layers of animation.
    // I need to do this since this method needs to requestAnimationFrame itself at all times it is running, so I could not limit its access to that step.
}

var stopIt = () =>{
    window.cancelAnimationFrame(requestID);
    dotButton.addEventListener("click", drawDot);
}

var dvdLogoSetup = function(){
    window.cancelAnimationFrame( requestID); // Uses the same requestID in order to have only "one animation" play at a time
    var rectWidth = 100;
    var rectHeight = 50;

    var rectX = Math.floor(Math.random() * (c.height - rectHeight));
    var rectY = Math.floor(Math.random() * (c.width - rectWidth));

    var xVel = Math.floor(Math.random(30));
    var yVel = Math.floor(Math.random(30));

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdLogo = function() {
        clear();
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        if (rectX <= 0 || rectX + rectHeight >= c.height){
            xVel *= -1;
        }
        if (rectY <= 0 || rectY + rectWidth >= c.width){
            yVel *= -1;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogoSetup);
    };
    dvdLogo();

}

dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
dvdButton.addEventListener("click", dvdLogoSetup);