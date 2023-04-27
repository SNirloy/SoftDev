// demo 2
// JS event propagation

var tds = document.getElementsByTagName('td'); // Gets all table data elements
var trs = document.getElementsByTagName('tr'); // Gets all table row elements
var table = document.getElementsByTagName('table')[0]; // Only the first table in the array of tables

var clicky = function(e) {
  alert( this.innerHTML );
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

for (x=0; x < trs.length; x++) {
  // trs[x].addEventListener('click', clicky);
}

table.addEventListener('click', clicky);

// They all have a listener attached

// Q: When user clicks on a cell, in what order will the pop-ups appear?
/*
I predict that the table responds first, then the table row, and finally the table data. 
This is based on how the DOM is structured, where an element has to be found through their parents.
Table holds Table Row holds Table Data

I got the order backwards.
The Table Data responded first, then the Row, then the Table. 
It was in the order of a "head first" recursion, where the recursion happens before the rest of the code is run.
Smallest Element first.

I did a little test where the middle event, for Table Rows, was diabled. Table data still responded first, and then the Table.
I guess that makes sense, knowing that the recursion happens before the eventListening.
*/