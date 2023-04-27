/*
Bread Wang, Sadi Nirloy 
*/

var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var saveButton = document.getElementById("buttonRect");
var stopButton = document.getElementById("buttonStop");

var ctx = c.getContext("2d");

var requestID;

var clear = (e) =>{
    ctx.clearRect(0, 0, c.width, c.height);
}

var radius = 0;
var growing = true;
var smaller = Math.min(c.width, c.height);

var drawDot = () => {
    window.cancelAnimationFrame(requestID); // to prevent the acceleration of animation
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
}

var stopIt = () =>{
    window.cancelAnimationFrame(requestID);
}

var drawSave = () =>{
    console.log("Gottem");
    window.cancelAnimationFrame( requestID); // Uses the same requestID in order to have only "one animation" play at a time
    
    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var rectWidth = 100;
    var rectHeight = 50;

    var rectX = Math.floor(Math.random() * (c.width - rectWidth));
    var rectY = Math.floor(Math.random() * (c.height - rectHeight));

    var xVel = Math.floor(Math.random(9)) + 1;
    var yVel = Math.floor(Math.random(9)) + 1;

    var dvdLogo = function() {
        clear();
        ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
        console.log(rectX + ", " + rectY);
        if (rectX <= 0 || rectX + rectWidth >= c.width){
            xVel *= -1;
        }
        if (rectY <= 0 || rectY + rectHeight >= c.height){
            yVel *= -1;
        }
        rectX += xVel;
        rectY += yVel;
        requestID = window.requestAnimationFrame(dvdLogo);
    };
    dvdLogo();
};

dotButton.addEventListener("click", drawDot);
saveButton.addEventListener("click", drawSave);
stopButton.addEventListener("click", stopIt);