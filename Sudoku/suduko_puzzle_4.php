<?php

// Create the Sudoku puzzle array
$puzzle = array(
    array(5, 3, 4, 6, 7, 8, 9, 1, 2),
    array(6, 7, 2, 1, 9, 5, 3, 4, 8),
    array(1, 9, 8, 3, 4, 2, 5, 6, 7),
    array(8, 5, 9, 7, 6, 1, 4, 2, 3),
    array(4, 2, 6, 8, 5, 3, 7, 9, 1),
    array(7, 1, 3, 9, 2, 4, 8, 5, 6),
    array(9, 6, 1, 5, 3, 7, 2, 8, 4),
    array(2, 8, 7, 4, 1, 9, 6, 3, 5),
    array(3, 4, 5, 2, 8, 6, 1, 7, 9)
);

// Function to print the Sudoku puzzle
function printPuzzle($puzzle, $blankCells) {
  // Iterate over rows
  for ($i = 0; $i < 9; $i++) {
    // Iterate over columns
    for ($j = 0; $j < 9; $j++) {
      // If the current cell is not in the list of blank cells, print its value followed by a space
      if (!in_array([$i, $j], $blankCells)) {
        echo $puzzle[$i][$j] . " ";
      }
      // Otherwise, print a space to indicate an empty cell
      else {
        echo "  ";
      }
      // If we are at the end of the row, print a newline character
      if ($j == 8) {
        echo "\n";
      }
    }
  }
}


// Call the function to print the puzzle
// Print the completed puzzle
echo "Completed puzzle:\n";
printPuzzle($puzzle, []);

echo "*********************: \n";

// Print the puzzle with missing numbers
//echo "\nPuzzle with missing numbers:\n";
//printPuzzle($puzzle);
$blankCells = [[0, 0], [1, 1], [2, 1], [3, 2], [4, 2], [5, 6], [6, 7], [7, 8], [8,9]];
printPuzzle($puzzle, $blankCells);

?>
