// demo 4
// JS event propagation

// Name the collections of TDs, TRs, and overall table
var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0];


var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  // Only the first one will react to the Event, irregardless if there is a true argument.
  e.stopPropagation();
};


//Q: Does the order in which the event listeners are attached matter?

//Predict, then test...
//Q: What effect does the boolean arg have in each?
//   (Leave exactly 1 version uncommented to test...)
/*
Prediction: 
To have a true argument in the addEventListener function changes the order of when the listener responds.
With true, it works FIFO, like a queue, where the largest element with a true listener will respond first, and then look to its children.
With false, it works FILO, like a stack, where the smallest/innermost element with a listener will respond first, and then look to its parents.
If mixed, all the trues will respond first in order of greatest to smallest, before the falses respond from the smallest to biggest.
*/

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky, true);
  //tds[x].addEventListener('click', clicky, false);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky, true);
  //trs[x].addEventListener('click', clicky, false);
}

table.addEventListener('click', clicky, true);
//table.addEventListener('click', clicky, false);
