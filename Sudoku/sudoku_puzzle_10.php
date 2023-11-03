<?php

// Function to create a Sudoku puzzle
function createPuzzle($concept) {
  // Initialize the puzzle with empty values
  switch($concept) {
    case "no-repeating-numbers":
      $puzzle = array_fill(0, 9, array_fill(0, 9, 0));
      for ($i = 0; $i < 9; $i++) {
        $nums = range(1,9);
        shuffle($nums);
        for ($j = 0; $j < 9; $j++) {
          $puzzle[$i][$j] = $nums[$j];
        }
      }
      break;
    case "sum-of-numbers":
  $puzzle = array_fill(0, 9, array_fill(0, 9, 0));
  for ($i = 0; $i < 9; $i++) {
    $remainingNumbers = range(1,9);
    shuffle($remainingNumbers);
    $rowSum = 0;
    for ($j = 0; $j < 9; $j++) {
      if($puzzle[$i][$j] == 0){
        $puzzle[$i][$j] = array_pop($remainingNumbers);
        $rowSum += $puzzle[$i][$j];
      }
    }
    if($rowSum != 45){
      return null;
    }
  }
  if (solvePuzzle($puzzle)) {
    return $puzzle;
  } else {
    return null;
  }
  break;
case "even-numbers-only":
    $puzzle = array_fill(0, 9, array_fill(0, 9, 0));
    $sum = 45;
    $numbers = range(2, 18, 2); // even numbers between 2 and 18
    shuffle($numbers); // shuffle the numbers to make it more random
    $k = 0; // to keep track of which number to use next
    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
            $puzzle[$i][$j] = $numbers[$k];
            $k++;
			while(in_array($puzzle[$i][$j], $puzzle[$i]) || in_array($puzzle[$i][$j], array_column($puzzle, $j))){
    $k = ($k >= count($numbers) -1) ? 0 : $k+1;
    $puzzle[$i][$j] = $numbers[$k];
	echo "check if the number is unique in the current row, column: " . $numbers[$k] . "\n";
}

            // // check if the number is unique in the current row, column
            // while(in_array($puzzle[$i][$j], $puzzle[$i]) || in_array($puzzle[$i][$j], array_column($puzzle, $j)) ){
                // if($k >= count($numbers)){
                    // $k = 0;
                // }
                // $puzzle[$i][$j] = $numbers[$k];
                // $k++;
				// echo "check if the number is unique in the current row, column: " . $numbers[$k];
            // }
        }
    }
    // check if the sum of each row, column is equal to $sum
    if (checkRowColSum($puzzle,$sum) && solvePuzzle($puzzle)) {
        echo "The target sum of each row,column is: " . $sum;
        return $puzzle;
    } else {
        return null;
    }
    break;

case "odd-numbers-only":
    $puzzle = array_fill(0, 9, array_fill(0, 9, 0));
    $sum = 45;
    $numbers = range(1, 19, 2); // odd numbers between 1 and 19
    shuffle($numbers); // shuffle the numbers to make it more random
    $k = 0; // to keep track of which number to use next
    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
            $puzzle[$i][$j] = $numbers[$k];
            $k++;
            // check if the number is unique in the current row, column, and diagonal
            while(in_array($puzzle[$i][$j], $puzzle[$i]) || in_array($puzzle[$i][$j], array_column($puzzle, $j)) || in_array($puzzle[$i][$j], getDiagonal($puzzle, $i, $j))){
                if($k >= count($numbers)){
                    $k = 0;
                }
                $puzzle[$i][$j] = $numbers[$k];
                $k++;
            }
        }
    }
    // check if the sum of each row, column, and diagonal is equal to $sum
    if (checkRowColDiagSum($puzzle,$sum) && solvePuzzle($puzzle)) {
        echo "The target sum of each row,column and diagonal is: " . $sum;
        echo"********************";
        echo "\n";
        return $puzzle;
    } else {
        return null;
    }
    break;

	case "diagonal-constraints":
        $puzzle = fillDiagonal($puzzle);
        if (solvePuzzle($puzzle)) {
          return $puzzle;
        } else {
          return null;
        }
        break;
    // Add cases for other concepts here
    default:
      // Return null if the concept passed as an argument is not recognized
      return null;
  }
   // Code to remove some of the known values and print the puzzle with hints
  return $puzzle;
}

function checkRowColSum($puzzle, $sum) {
    for ($i = 0; $i < 9; $i++) {
        if (array_sum($puzzle[$i]) != $sum) {
            return false;
        }
    }
    for ($j = 0; $j < 9; $j++) {
        $col = array();
        for ($i = 0; $i < 9; $i++) {
            $col[] = $puzzle[$i][$j];
        }
        if (array_sum($col) != $sum) {
            return false;
        }
    }
    return true;
}

function checkRowColDiagSum($puzzle, $sum) {
for ($i = 0; $i < 9; $i++) {
if (array_sum($puzzle[$i]) != $sum) {
return false;
}
}
for ($j = 0; $j < 9; $j++) {
$col = array();
for ($i = 0; $i < 9; $i++) {
$col[] = $puzzle[$i][$j];
}
if (array_sum($col) != $sum) {
return false;
}
}
if(array_sum(getDiagonal($puzzle, 0, 0, 'top-left-to-bottom-right')) != $sum) {
return false;
}
if(array_sum(getDiagonal($puzzle, 0, 8, 'top-right-to-bottom-left')) != $sum) {
return false;
}
return true;
}

// // Use the checkRowColDiagSum function to check if the puzzle is valid
// if (checkRowColDiagSum($puzzle, $sum)) {
// echo "The target sum of each row, column, and diagonal is: " . $sum;
// return $puzzle;
// } else {
// return null;
// }
// break;
// }
// }


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

function getDiagonal($puzzle, $row, $col, $direction = 'top-left-to-bottom-right') {
$diagonal = array();
if ($direction == 'top-left-to-bottom-right') {
while ($row < 9 && $col < 9) {
$diagonal[] = $puzzle[$row][$col];
$row++;
$col++;
}
} else {
while ($row < 9 && $col >= 0) {
$diagonal[] = $puzzle[$row][$col];
$row++;
$col--;
}
}
return $diagonal;
}

function fillDiagonal(&$puzzle) {
  //fill the diagonal cells with random numbers that follows the no-repeating rule.
  for ($i = 0; $i < 9; $i++) {
    $num = rand(1, 9);
    while (!isValid($puzzle, $i, $i, $num)) {
      $num = rand(1, 9);
    }
    $puzzle[$i][$i] = $num;
  }
  for ($i = 0; $i < 9; $i++) {
    $num = rand(1, 9);
    while (!isValid($puzzle, 8-$i, $i, $num)) {
      $num = rand(1, 9);
    }
    $puzzle[8-$i][$i] = $num;
  }
  return $puzzle;
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

function printPuzzle($puzzle) {
	// Iterate over rows
    for ($i = 0; $i < 9; $i++) {
		// Iterate over columns
        for ($j = 0; $j < 9; $j++) {
			// If the current cell is not empty, print its value followed by a space
            if ($puzzle[$i][$j] != 0) {
                printf("%2d ", $puzzle[$i][$j]);
            } else {
                echo "   ";
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
$puzzle = createPuzzle('even-numbers-only');

// Call the printPuzzle function to print the puzzle -- prints solved version
printPuzzle($puzzle);
  echo "*****************";
  echo "\n";
  echo "*****************";
  echo "\n";

// Call the createGame function to print the unsolved puzzle with hints
createGame($puzzle, 25, true);

?>
