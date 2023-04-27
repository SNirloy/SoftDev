// demo 1
// JS event propagation

var tds = document.getElementsByTagName('td'); // Looks specifically for the table data, not row nor the full table

var clicky = function(e) {
  alert( this.innerHTML ); // Tells us the HTML of the element we clicked.
};

for (var x=0; x < tds.length; x++) {
  tds[x].addEventListener('click', clicky);
}

/*
I predict that clicking on an element of the table will get us the name of the star wars character inside the table.
This should bypasses the table and table row elements.

My prediction was correct. With only the most inner element holding an eventListener, only they are allowed to respond, not their parents.
*/