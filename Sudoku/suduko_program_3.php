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
function printPuzzle($puzzle) {
  // Iterate over rows
  for ($i = 0; $i < 9; $i++) {
    // Iterate over columns
    for ($j = 0; $j < 9; $j++) {
      // Print the value of the current cell followed by a space
      echo $puzzle[$i][$j] . " ";
      // If we are at the end of the row, print a newline character
      if ($j == 8) {
        echo "\n";
      }
    }
  }
}

// Call the function to print the puzzle
printPuzzle($puzzle);

?>
