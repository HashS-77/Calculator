# Calculator GUI

A simple graphical calculator application built with Python and Tkinter.

## Description

This is a desktop calculator application with a user-friendly GUI that allows you to perform basic arithmetic operations. It features a clean interface with buttons for digits, operators, and functions.

## Features

- **Number Buttons**: Buttons for digits 0-9 to enter numbers
- **Arithmetic Operations**: Support for addition (+), subtraction (-), multiplication (*), and division (/)
- **Clear Button**: Clear the display with the "C" button
- **Equals Button**: Calculate the result of your expression
- **Keyboard Support**: Press Enter to calculate the result
- **Error Handling**: Displays "Error" if an invalid expression is entered

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. Tkinter should be included with your Python installation

## Usage

1. Run the calculator:
   ```
   python Calculator.py
   ```

2. Use the buttons to enter numbers and operators
3. Click the "=" button or press Enter to calculate the result
4. Click "C" to clear the display

## How It Works

- **GUI Layout**: The calculator uses Tkinter to create a grid-based button layout with a text entry field at the top
- **Calculation**: The `calculate()` method uses Python's `eval()` function to evaluate mathematical expressions
- **Error Handling**: If an invalid expression is entered, the calculator displays "Error"

## Button Layout

```
| 1 | 2 | 3 | +  |
| 4 | 5 | 6 | -  |
| 7 | 8 | 9 | *  |
| C | 0 | = | /  |
```

## Example

1. Click buttons: 5 + 3
2. Click "=" or press Enter
3. Result: 8

## License

This project is open source and available for personal and educational use.