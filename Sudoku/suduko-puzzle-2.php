<?php

// Function to check if a given number is valid for a given position in the Sudoku grid
ini_set("error_log", "D:\Scraping-tool\suduko_errors_log.txt");

function isValid($grid, $row, $col, $num) {
  // Check if $num is already present in the same row
  for ($c = 0; $c < 9; $c++) {
    if ($grid[$row][$c] == $num) {
      return false;
    }
  }

  // Check if $num is already present in the same column
  for ($r = 0; $r < 9; $r++) {
    if ($grid[$r][$col] == $num) {
      return false;
    }
  }

  // Check if $num is already present in the same 3x3 subgrid
  $startRow = floor($row / 3) * 3;
  $startCol = floor($col / 3) * 3;
  for ($r = $startRow; $r < $startRow + 3; $r++) {
    for ($c = $startCol; $c < $startCol + 3; $c++) {
      if ($grid[$r][$c] == $num) {
        return false;
      }
    }
  }

  // If no conflicts, $num is valid for the given position
  return true;
}

// Depth-first search function to generate a Sudoku puzzle
/*function generatePuzzle($grid, $row, $col) {
  // If all cells are filled, the puzzle is solved
  if ($row == 9) {
    return true;
  }

  // If the current cell is not empty, move on to the next cell
  if ($grid[$row][$col] != 0) {
    if ($col == 8) {
      if (generatePuzzle($grid, $row + 1, 0)) {
        return true;
      }
    } else {
      if (generatePuzzle($grid, $row, $col + 1)) {
        return true;
      }
    }
    return false;
  }

  // Try filling the current cell with a number from 1 to 9
  for ($num = 1; $num <= 9; $num++) {
    if (isValid($grid, $row, $col, $num)) {
      $grid[$row][$col] = $num;

      // Recurse to the next cell
      if ($col == 8) {
        if (generatePuzzle($grid, $row + 1, 0)) {
          return true;
        }
      } else {
        if (generatePuzzle($grid, $row, $col + 1)) {
          return true;
        }
      }
    }
  }

  // No valid number was found, reset the current cell and backtrack
  $grid[$row][$col] = 0;
  return false;
}*/

// Depth-first search function to generate a Sudoku puzzle
function generatePuzzle($grid, $row, $col, $fillCell = true, $depth = 0) {
  // If all cells are filled, the puzzle is solved
  if ($row == 9) {
    return true;
  }

  // If the maximum recursion depth is reached, return false
  if ($depth > 1000) {
    error_log('Maximum recursion depth reached', 3, 'D:\Scraping-tool\suduko_errors_log.txt');
    return false;
  }

  // If the current cell should not be filled, move on to the next cell
  if (!$fillCell) {
    if ($col == 8) {
      error_log('Moving on to the next cell (current cell should not be filled)', 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      error_log('Current grid state: ' . print_r($grid, true) . "\n", 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      return generatePuzzle($grid, $row + 1, 0, true, $depth + 1);
    } else {
      error_log('Moving on to the next cell (current cell should not be filled)', 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      error_log('Current grid state: ' . print_r($grid, true) . "\n", 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      return generatePuzzle($grid, $row, $col + 1, true, $depth + 1);
    }
  }

  // Try filling the current cell with a number from 1 to 9
  for ($num = 1; $num <= 9; $num++) {
    error_log('Trying to fill current cell with number ' . $num, 3, 'D:\Scraping-tool\suduko_errors_log.txt');
    error_log('Current grid state: ' . print_r($grid, true) . "\n", 3, 'D:\Scraping-tool\suduko_errors_log.txt');
    if (isValid($grid, $row, $col, $num)) {
      $grid[$row][$col] = $num;

      // Recurse to the next cell
      if ($col == 8) {
        if (generatePuzzle($grid, $row + 1, 0, true, $depth + 1)) {
          return true;
        }
      } else {
        if (generatePuzzle($grid, $row, $col + 1, true, $depth + 1)) {
          return true;
        }
      }
    }
  }

  // No valid number was found, reset the current cell and backtrack if needed
  $grid[$row][$col] = 0;
  if ($row > 0 || $col > 0) {
    if ($col == 0) {
      error_log('No valid number found, resetting current cell and backtracking', 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      error_log('Current grid state: ' . print_r($grid, true) . "\n", 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      return generatePuzzle($grid, $row - 1, 8, false, $depth + 1);
    } else {
      error_log('No valid number found, resetting current cell and backtracking', 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      error_log('Current grid state: ' . print_r($grid, true) . "\n", 3, 'D:\Scraping-tool\suduko_errors_log.txt');
      return generatePuzzle($grid, $row, $col - 1, false, $depth + 1);
    }
  }

  return false;
}


// Initialize an empty 9x9 grid
$grid = array_fill(0, 9, array_fill(0, 9, 0));

// Generate a full Sudoku puzzle
generatePuzzle($grid, 0, 0);

// Choose a random number of cells to remove (between 17 and 20)
$numRemoved = rand(17, 20);

// Remove a random cell $numRemoved times
for ($i = 0; $i < $numRemoved; $i++) {
  $row = rand(0, 8);
  $col = rand(0, 8);
  $grid[$row][$col] = 0;
}

// Display the final puzzle to the user
echo "Sudoku Puzzle:\n";
for ($row = 0; $row < 9; $row++) {
  for ($col = 0; $col < 9; $col++) {
    echo $grid[$row][$col] . " ";
  }
  echo "\n";
}
