// demo 3
// JS event propagation

var tds = document.getElementsByTagName('td');
var trs = document.getElementsByTagName('tr');
var table = document.getElementsByTagName('table')[0]; // Same as before, with all elements with a listener

var clicky = function(e) {
  alert( this.innerHTML );
  //Q: What will happen when next line is uncommented?
  e.stopPropagation();
  // I predict that this will prevent parents from responding to the event, basing this of off a head-first recursion.
  // But knowing the rest, it only allows the first one with precedence given.
  // As the second preduction
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  trs[x].addEventListener('click', clicky);
}

// With two true arguments, it appears that the precedence is parent first, a queue, as opposed to the stack like construction.


//Predict, then test...
//Q: What effect does the boolean arg have?
//   (Leave exactly 1 version uncommented to test...)
// It appears to give precedence.

//table.addEventListener('click', clicky, true);
table.addEventListener('click', clicky, true);

// Q: When user clicks on a cell, in what order will the pop-ups appear?
/*
I accidently tested this without predicting, but I would never have guessed it.
When the argument true is added, the order is table, data, row.
Seeing as how table is the only one with the true, I believe the true argument gives it a precedence to its children. Afterwards, standard recursion order applies afterwards.

I predict that false arguments is the default, where no precedence is added.

Just as predicted.
*/