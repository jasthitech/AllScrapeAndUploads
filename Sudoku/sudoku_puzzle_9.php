<?php

// Function to create a Sudoku puzzle
// function createPuzzle() {
  // // Initialize the puzzle with empty values
  // $puzzle = array_fill(0, 9, array_fill(0, 9, 0));

  // // Generate a random set of known values
  // for ($i = 0; $i < 9; $i++) {
    // for ($j = 0; $j < 9; $j++) {
      // $puzzle[$i][$j] = rand(1, 9);
    // }
  // }

  // // Use a backtracking algorithm to fill in the remaining empty cells
  // if (solvePuzzle($puzzle)) {
    // return $puzzle;
  // } else {
    // return null;
  // }
// }

function createPuzzle() {
  // Initialize the puzzle with empty values
  $puzzle = array_fill(0, 9, array_fill(0, 9, 0));

  // Use a backtracking algorithm to generate a fully solved puzzle with no repeating numbers
  if (solvePuzzle($puzzle)) {
    // Remove a certain number of cells from the puzzle to create the final puzzle for the user
    // for ($i = 0; $i < 35; $i++) {
      // $randRow = rand(0, 8);
      // $randCol = rand(0, 8);
      // $puzzle[$randRow][$randCol] = 0;
    // }
    return $puzzle;
  } else {
    return null;
  }
}


// Function to solve the Sudoku puzzle using a backtracking algorithm
function solvePuzzle(&$puzzle) {
  for ($i = 0; $i < 9; $i++) {
    for ($j = 0; $j < 9; $j++) {
      // If the current cell is empty, try filling it with a number from 1 to 9
      if ($puzzle[$i][$j] == 0) {
        for ($k = 1; $k <= 9; $k++) {
          // Check if the number is valid for the current cell
          if (isValid($puzzle, $i, $j, $k)) {
            // If it is, assign the number to the cell and try solving the rest of the puzzle
            $puzzle[$i][$j] = $k;
            if (solvePuzzle($puzzle)) {
              return true;
            }
            // If the puzzle cannot be solved, backtrack and try a different number for the cell
            $puzzle[$i][$j] = 0;
          }
        }
        return false;
      }
    }
  }
  return true;
}

// Function to check if a given number is valid for a given cell
function isValid($puzzle, $row, $col, $num) {
  // Check if the number appears in the same row
  for ($i = 0; $i < 9; $i++) {
    if ($puzzle[$row][$i] == $num) {
      return false;
    }
  }
  // Check if the number appears in the same column
  for ($i = 0; $i < 9; $i++) {
    if ($puzzle[$i][$col] == $num) {
      return false;
    }
  }
  // Check if the number appears in the same 3x3 subgrid
  $startRow = $row - $row % 3;
  $startCol = $col - $col % 3;
    for ($i = $startRow; $i < $startRow + 3; $i++) {
    for ($j = $startCol; $j < $startCol + 3; $j++) {
      if ($puzzle[$i][$j] == $num) {
        return false;
      }
    }
  }
  return true;
}

// Function to print the Sudoku puzzle
function printPuzzle($puzzle) {
  // Iterate over rows
  for ($i = 0; $i < 9; $i++) {
    // Iterate over columns
    for ($j = 0; $j < 9; $j++) {
      // If the current cell is not empty, print its value followed by a space
      if ($puzzle[$i][$j] != 0) {
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

function createGame($puzzle, $numBlankCells, $displayHints) {
  $blankCells = array();
  $possibleValues = array();
  for ($i = 0; $i < 9; $i++) {
    for ($j = 0; $j < 9; $j++) {
      $possibleValues[$i][$j] = 0;
    }
  }

  // Randomly choose the cells to make blank
  while (count($blankCells) < $numBlankCells) {
    $randRow = rand(0, 8);
    $randCol = rand(0, 8);
    if ($puzzle[$randRow][$randCol] != 0 && !in_array([$randRow, $randCol], $blankCells)) {
      $blankCells[] = [$randRow, $randCol];
      $puzzle[$randRow][$randCol] = 0;
    }
  }

  // Calculate the number of possible values for each blank cell
  if($displayHints){
    for ($i = 0; $i < 9; $i++) {
      for ($j = 0; $j < 9; $j++) {
        if ($puzzle[$i][$j] == 0) {
          for ($k = 1; $k <= 9; $k++) {
            if (isValid($puzzle, $i, $j, $k)) {
              $possibleValues[$i][$j]++;
            }
          }
        }
      }
    }
  }
  // Print the new puzzle with blank cells
  printPuzzle($puzzle);
  echo "*****************";
  echo "\n";
  echo "*****************";
  echo "\n";
  
  // Print the hints for the blank cells
  if ($displayHints) {
    for ($i = 0; $i < count($blankCells); $i++) {
      $row = $blankCells[$i][0];
      $col = $blankCells[$i][1];
      echo "Hint for cell [" . ($row + 1) . ", " . ($col + 1) . "]: " . $possibleValues[$row][$col] . " possible values\n";
    }
  }
}

// Call the createPuzzle function to generate a new Sudoku puzzle
$puzzle = createPuzzle();

// Call the printPuzzle function to print the puzzle -- prints solved version
printPuzzle($puzzle);
  echo "*****************";
  echo "\n";
  echo "*****************";
  echo "\n";

// Call the createGame function to print the unsolved puzzle with hints
createGame($puzzle, 30, true);

?>
