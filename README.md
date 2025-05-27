In the repository, you’ll find three iterations of the project in the corresponding branches: `checkpoint_1`, `checkpoint_2`, and `checkpoint_3`.

- **`checkpoint_1`**: Construction of an NFA/regular expression → DFA.  
  An example of how to use the code from this stage is provided in `checkpoint_2` in the file  
  `scanner_folder/dfa_for_scanner.py`, within the function `dfa_for_scanner`.

- **`checkpoint_2`**: Scanner construction.  
  To test the scanner on your own examples, add one or more lines to `scanner_input.txt` and then run `test_scanner.py`.  
  The scanner’s output will be printed to the console.

- **`checkpoint_3`**: Basic interpreter. The interpreter supports:  
  1. Declaration of variables with simultaneous assignment of values of type `INT`, `BOOL`, or `STRING` (for example, `a = true`)  
  2. A `print` function analogous to Python’s  
  3. An `if` construct in the form  
     ```  
     if (condition) {  
       // ...  
     }  
     ```  
     (no `else`)  
  4. A `while` loop in the form  
     ```  
     while (condition) {  
       // ...  
     }  
     ```  

  To test the interpreter, place your program code in `input_driver.txt` and run `Driver.py`.  
  The interpreter’s output will appear in the console, and the parse tree will be written to `output_driver.txt`.
