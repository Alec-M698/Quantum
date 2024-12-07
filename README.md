
# Quantum Programming Language

Quantum is a versatile and powerful programming language designed for simplicity and ease of use. It supports various features such as variables, data types, control flow statements, functions, input/output operations, file handling, and more.

Quantum provides support for Visual Studio Code.
It can run on any operating system, text editor, or
IDE that has or supports Python.

### Prerequisites 
- [Visual Studio Code](https://code.visualstudio.com/) 
- [Python](https://www.python.org/) (for running the Quantum interpreter)

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Running Quantum Code](#running-quantum-code)
   - [Using the Quantum REPL](#using-the-quantum-repl)
4. [Variable Types](#variable-types)
5. [Data Types](#data-types)
6. [Control Flow](#control-flow)
   - [If Statements](#if-statements)
   - [Switch/Case Statements](#switchcase-statements)
   - [Loops](#loops)
7. [Functions](#functions)
8. [Input and Output](#input-and-output)
9. [File Handling](#file-handling)
10. [Comments](#comments)
11. [Examples](#examples)
12. [Acknowledgments](#acknowledgments)
13. [License](#license)
14. [Contributing](#contributing)

## Introduction
Quantum is designed to be easy to learn and use, making it an excellent choice for beginners and experienced developers alike. It provides a clean and straightforward syntax, allowing you to focus on solving problems rather than dealing with complex language features.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/quantum.git
   cd quantum
   ```
2. Install the Code Runner extension:
    - Open Visual Studio Code.
    - Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+X.
    - Search for "Code Runner" by Jun Han and click on the "Install" button.

3. Configure Code Runner:
    - Open the settings by clicking on the gear icon in the lower left corner and selecting "Settings".
    - Search for "Code Runner: Executor Map" in the settings search bar.
    - Click on "Edit in settings.json" to open the settings.jsonfile.
    - Add the following configuration to the settings.json file:

        ```json
        {
            "code-runner.executorMap": {
                "quantum": "python path/to/quantum-lang/quantum.py"
            },
            "code-runner.runInTerminal": true,
            "code-runner.saveFileBeforeRun": true
        }
        ```

## Usage

### Running Quantum Code
_VSCode only_

1. Using the run button in VSCode
Create a file with a .qt or .quantum extension.
Click the run button in the top right corner of the VSCode window.

### Using the Quantum REPL
Quantum also provides a REPL (Read-Eval-Print Loop) for interactive code execution. To start the REPL, use the `repl.py` script:

```sh
python src/repl.py
```

In the REPL, you can write Quantum code and see the results immediately. Type `.exit` to exit the REPL.

Example REPL session:

```sh
Quantum REPL. Type .exit to exit.
>>> var x = 10
>>> var y = 20
>>> func add()
...     var result = x + y
...     print(result)
... endfunc
>>> add()
30
>>> .exit
```

## Variable Types
Quantum supports dynamic typing, meaning variables can hold values of any type, and their type can change at runtime.

## Data Types
Quantum supports the following data types:
- **Integer**: Whole numbers (e.g., `10`, `-5`)
- **Float**: Decimal numbers (e.g., `3.14`, `-0.001`)
- **String**: Text enclosed in double quotes (e.g., `"Hello, World!"`)
- **Boolean**: `true` or `false`
- **List**: Ordered collection of elements (e.g., `[1, 2, 3]`)
- **Dictionary**: Key-value pairs (e.g., \
`{"name": "John", "age": 30}`)

## Control Flow

### If Statements
If statements are used to execute code based on a condition.

```python
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")
endif
```

### Switch/Case Statements
Switch/case statements are used to execute code based on the value of a variable.

```python
var day = 3
switch day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
endswitch
```

### Loops
Quantum supports `for` and `while` loops for repetitive tasks.

#### For Loop
```python
for i in range(1, 5):
    print("Loop iteration: " + str(i))
endfor
```

#### While Loop
```python
var count = 0
while count < 5:
    print("Count is: " + str(count))
    var count = count + 1
endwhile
```

## Functions
Functions are defined using the `func` keyword followed by the function name and an optional list of parameters.

```python
func add(a, b)
    var result = a + b
    return result
endfunc

var sum = add(10, 20)
print(sum)
```

## Input and Output
Quantum supports input and output operations using the `input` and `print` functions.

### Input
```python
var name = input("What's your name?")
print("Hello " + name + "!")
```

### Output
```python
print("Hello, World!")
```

## File Handling
Quantum supports reading from and writing to files.

### Read File
```python
var content = read_file("example.txt")
print(content)
```

### Write File
```python
write_file("example.txt", "Hello, Quantum!")
```

## Comments
Comments are used to add explanatory notes to the code. Quantum supports single-line and multi-line comments.

> **Note**<br>
A multi-line comment in Quantum **must** span at least two lines 
OR all of your code will be in comments, from the start of the multi-line 
comment to the end of the file.

### Single-Line Comment
```python
# This is a single-line comment
```

### Multi-Line Comment
```javascript
/*
This is a
multi-line comment
*/
```

## Examples
Here are some example Quantum programs demonstrating various features:

### Example 1: Basic Operations
```js
var x = 10
var y = 20

func add()
    var result = x + y
    print(result)
endfunc

add()
```

### Example 2: Conditional Statements
```python
var x = 10
var y = 20

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")
endif
```

### Example 3: Loops
```python
# For Loop
for i in range(1, 5):
    print("Loop iteration: " + str(i))
endfor

# While Loop
var count = 0
while count < 5:
    print("Count is: " + str(count))
    var count = count + 1
endwhile
```

### Example 4: File Handling
```python
# Write to a file
write_file("output.txt", "Hello, Quantum!")

# Read from a file
var content = read_file("output.txt")
print(content)
```

## License
Quantum is open source and licensed under the MIT License.

## Contributing
If you'd like to contribute to Quantum, please fork the repository and submit a pull request. We appreciate any help we can get!
