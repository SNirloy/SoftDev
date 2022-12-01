# Table Corner: Sadi Nirloy and Thomas Zhang
## Foundation Front End Frameworks
### Grid XY
- In order to make the most of flex boxes in css, Foundation has the grid-x and grid-y classes for div tags.
	- grid-x represents a row, and grid-y represents a column. Both adjust to the size of your screen
```
	<div class="grid-x">

	</div>
	<div class="grid-y">

	</div>
```
- These rows and columns are populated by cells, another div class.
```
	<div class="grid-x">
	  <div class="cell">A cell to take up the entire row</div>
	  <div class="cell">Taking up the next row</div>
	</div>

	<div class="grid-y">
	  <div class="cell">A cell to take up the entire row</div>
	  <div class="cell">Still on the next row</div>
	</div>
```
- 
	- The cells in grid-x can be assigned a size to take up only part of the row. A full row has a size of 12 units.
	- In the example, you'll see a word that describes size, like small, big, or medium. Not exactly sure what it does at this point. Just keep things to small for now.
```
	<div class="grid-x">
	  <div class="cell big-4">One-third of the row</div>
	  <div class="cell small-8">The rest</div>
	</div>

	<div class="grid-y">
	  <div class="cell small-4">Whole Row</div>
	  <div class="cell small-2">The next row</div>
	</div>
```
- 
	- In the grid-y, you'll see how the cell still stretches across the entire row. Not exactly sure why it does that.
- To make an actual grid: Make a grid-x that has grid-ys within the cells
```	
	<div class="grid-x">
	  <div class="cell small-2">
	    <div class="grid-y">
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	    </div>
	  </div>
	  <div class="cell small-6">
	    <div class="grid-y">
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	    </div>
	  </div>
	  <div class="cell small-4">
	    <div class="grid-y">
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	      <div class="cell">
		X
	      </div>
	    </div>
	  </div>
	</div>
```

