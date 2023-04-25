//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode == "rect") {
        mode = "circ";
    }
    else {
        mode = "rect";
    }
    var bToggler = document.getElementById("buttonToggle");
    bToggler.innerHTML = mode;
}

var drawRect = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillRect(mouseX, mouseY, 10, 10);
}

var drawCircle = function(e) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "black"; //circle color
    ctx.strokeStyle = "black";
    ctx.arc(mouseX, mouseY, 10, 0, 2*Math.PI);
    ctx.fill();
    ctx.closePath();
}

//var draw = function(e){}
var draw = (e) => {
    if( mode == "circ"){
        drawCircle(e);
    }
    else{
        drawRect(e);
    }
}

//var wipeCanvas - function(){}
var wipeCanvas = () => {
    ctx.clearRect(0, 0, c.width, c.height);
}

c.addEventListener("click", draw) //passes the mouse event as parameter for the function

var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click', wipeCanvas);