// Buffalos buffalo Buffalo :: James Yu, Sadi Nirloy
// SoftDev pd8
// K28 -- Getting more comfortable with the dev console and the DOM
// 2023-04-05w
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30;
  return j+x;
};
//adds 30 to the input

//instantiate an object
// Object o can be printed
var o = { 'name' : 'Thluffy' , // o.name
          age : 1024 , // o.age
          items : [10, 20, 30, 40], // o.items, individual values can be like any other list: o.items[i]
          morestuff : {a : 1, b : 'ayo'}, // o.morestuff gets the inner object, and the dot notation can be stacked: o.morestuff.a
          func : function(x) { // o.func(input)
            return x+30;
          }
        };

var addItem = function(text) {
  var list = document.getElementById("thelist"); //thelist is the id for the list in the html file
    // To grab a part of the html by the user given id
    // You can console.log(document) in order to get this object/dictionary of the whole HTML document
    // Something similar appears when you console.log(document.getElementById("thelist"))
    // Is this the DOM? A DOM is described as an API, and this console.log produces a dictionary. I even found a line: implementation: DOMImplementation
    // I cannot seem to find where all the "Elements" are stored in the dict. There is a thing for firstChild and firstElementChild.
    // So this firstChild is the Doctype declaration and a next sibling, which is the comment at the top. Is this because they are both comment like structures with <!> syntax?
    // And firstChildElements then also has a firstChild key inside itself, so is this how the JS can search through the HTML file?
  var newitem = document.createElement("li"); // Adds a tag to the HTML of this variable
  newitem.innerHTML = text;
    // This is one of the keys I found when printing document
  list.appendChild(newitem);
    // Supports my idea that the firstChild is the next element (IDK if the terminology is correct). There is a lastChild and lastElementChild as well in the document.
};
//adds a the text you input to the list
//despite changing the html in the console, the update does not appear in the page

var removeItem = function(n) {
  var listitems = document.getElementsByTagName('li'); // it doesn't specify which list it removes from
    // So if you have a list earilier in the code, the code'll include them when counting. 
    // Perhaps we could replace document with a document.getElementById(), to pick a starting point in the DOM to look through
  listitems[n].remove();
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};
//it only turns the first and the last item red, not the entire list

var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};
//stripe also only works on the first and last items. Maybe instead of adding, you replace the class.

//insert your implementations here for...
// FIB
var fib = function(n){
  if (n < 2){
      return n;
  }
  else{
      return fib(n - 1) + fib(n - 2);
  }
};

var dasbut = document.getElementById("b"); 
dasbut.addEventListener('click', ()=>{
	console.log(fib(20));
});

// FAC
var fact = function(n){
  if (n < 2){
      return 1;
  }
  else{
      return n * fact(n - 1);
  }
};

var dasbut = document.getElementById("a"); 
dasbut.addEventListener('click', ()=>{
	console.log(fac(20));
});


// GCD
var gcd = function(a,b){
  if(a == 0){
    return b;
  }
  if (b == 0){
    return a;
  }
  else{
    return gcd(b, a%b);
  }
}

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => { //it makes it act like a function without the funtion keyword
  // body
  retVal = param1+param2;
  return retVal;
}



