<h1 align="center">README</h1>

<p align="center">This README file serves as a generator for Markdown formatted READMEs. It contains parsers for LL(1) and LR(1) grammars along with input processing capabilities.</p>

## Table of Contents
- [LL(1) Parser](#ll1-parser)
  - [LL Grammar File Parsing](#ll-grammar-file-parsing)
  - [LL Parsing Algorithm](#ll-parsing-algorithm)
  - [LL Parsing Process](#ll-parsing-process)
- [LR(1) Parser](#lr1-parser)
  - [LR Grammar File Parsing](#lr-grammar-file-parsing)
  - [LR Parsing Algorithm](#lr-parsing-algorithm)
  - [LR Parsing Process](#lr-parsing-process)
- [Input Processing](#input-processing)
- [Running the Parser](#running-the-parser)

## LL(1) Parser

### LL Grammar File Parsing

The LL grammar file is read from the file 📄 "ll.txt". The grammar rules are extracted and stored in a dictionary called `ll_table`. The non-terminals are stored in a list called `ll_non_terminals`.

### LL Parsing Algorithm

The LL parsing algorithm is implemented using the `ll_parser` function. The input string is parsed according to the LL(1) parsing table stored in `ll_table`. The algorithm follows the steps below:

1. Initialize the stack with the end-of-input marker 💲.
2. Print the initial stack, input, and action.
3. Reverse the input string to handle right-to-left parsing.
4. Iterate until the stack is empty:
   - Get the top of the stack.
   - Get the current input symbol.
   - If the top matches the current input symbol, remove them from the stack and input.
   - If there is a production rule for the top and current input symbol in the LL(1) parsing table, apply the production rule by replacing the top with the right-hand side of the rule.
   - If the production rule is "ϵ" (epsilon), continue to the next iteration.
   - If none of the above conditions are met, the input string is rejected.
5. If the stack is empty and the input string is fully consumed, the input string is accepted.

### LL Parsing Process

The LL parsing process is as follows:

1. Read LL(1) parsing table from file 📄 "ll.txt".
2. Read input strings from file 📄 "input.txt".
3. For each input string:
   - Parse the input string using the LL parsing algorithm.
   - Print the parsing steps, including the stack, input, and actions taken.
   - If the input string is accepted, mark it as ✅ accepted.
   - If the input string is rejected, mark it as ❌ rejected.

## LR(1) Parser

### LR Grammar File Parsing

The LR grammar file is read from the file 📄 "lr.txt". The parsing table is extracted and stored in a dictionary called `lr_table`. The LR states, actions, and gotos are stored in separate lists called `lr_state`, `lr_action`, and `lr_goto`, respectively.

### LR Parsing Algorithm

The LR parsing algorithm is implemented using the `lr_parser` function. The input string is parsed according to the LR(1) parsing table stored in `lr_table`. The algorithm follows the steps below:

1. Initialize the state stack with the initial state.
2. Reverse the input string to handle right-to-left parsing.
3. Iterate until the input stack is empty:
   - Get the current input symbol.
   - If the current state and input symbol have an action in the LR(1) parsing table, perform the action:
     - If the action is a shift operation, change to the new state and shift the input symbol.
     - If the action is a reduce operation, replace the reduced symbols with the left-hand side of the production rule.
     - If the action is "ACCEPT," the input string is accepted.
   - If there is no action for the current state and input symbol, the input string is rejected.
4. If the input stack is empty and there are no more actions to perform, the input string is rejected.

### LR Parsing Process

The LR parsing process is as follows:

1. Read LR(1) parsing table from file 📄 "lr.txt".
2. Read input strings from file 📄 "input.txt".
3. For each input string:
   - Parse the input string using the LR parsing algorithm.
   - Print the parsing steps, including the state stack, read symbol, input, and actions taken.
   - If the input string is accepted, mark it as ✅ accepted.
   - If the input string is rejected, mark it as ❌ rejected.

## Input Processing

The input strings are read from the file 📄 "input.txt". Each input string is processed based on its type (LL or LR) and passed to the corresponding parser.

### LL Input Processing

The LL input strings are processed using the LL parsing algorithm. The input string is split into tokens based on the defined grammar rules. The LL parsing algorithm is then applied to parse the input string.

### LR Input Processing

The LR input strings are processed using the LR parsing algorithm. The input string is reversed to handle right-to-left parsing. The LR parsing algorithm is then applied to parse the input string.

## Running the Parser

To run the parser:

1. Ensure that the LL grammar file is named 📄 "ll.txt", the LR grammar file is named 📄 "lr.txt", and the input file is named 📄 "input.txt".
2. Execute the code.
3. The parser will read the grammar files and input file and perform the LL(1) and LR(1) parsing processes.
4. The parsing steps and results will be displayed for each input string.

Please refer to the code for detailed implementation and additional information.
